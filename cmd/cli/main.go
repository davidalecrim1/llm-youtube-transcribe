package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/joho/godotenv"
)

func main() {
	err := godotenv.Load("../../.env")
	if err != nil {
		log.Fatalf("Error loading .env file: %v", err)
	}

	ctx := context.Background()

	client := &http.Client{}
	llm := NewLLM(
		client,
		WithEndpoint(os.Getenv("LM_STUDIO_URL")))

	models, err := llm.GetModels(ctx)
	if err != nil {
		log.Fatalf("Error getting models: %v", err)
	}

	response, err := json.Marshal(models)
	if err != nil {
		log.Fatalf("Error parsing response from models: %v", err)
	}

	fmt.Println(string(response))
}

type LLM struct {
	client   *http.Client
	endpoint string
}

type LLMOption func(*LLM)

func WithEndpoint(endpoint string) LLMOption {
	return func(llm *LLM) {
		llm.endpoint = endpoint
	}
}

func NewLLM(client *http.Client, options ...LLMOption) *LLM {
	llm := &LLM{client: client}

	for _, opt := range options {
		opt(llm)
	}

	return llm
}

func (l *LLM) GetModels(ctx context.Context) (*LLMGetModelsResponse, error) {
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, l.endpoint+"/v1/models", nil)
	if err != nil {
		return nil, err
	}

	req.Header.Set("Content-Type", "application/json")

	res, err := l.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer res.Body.Close()

	data := LLMGetModelsResponse{}
	if err := json.NewDecoder(res.Body).Decode(&data); err != nil {
		return nil, err
	}

	return &data, nil
}
