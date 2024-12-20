package main

type LLMGetModelsResponse struct {
	Data   []LLMGetModelsResponseData `json:"data"`
	Object string                     `json:"object"`
}

type LLMGetModelsResponseData struct {
	Id      string `json:"id"`
	Object  string `json:"object"`
	OwnedBy string `json:"owned_by"`
}
