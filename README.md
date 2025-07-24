# nbot_search

## Introduction

Welcome to the nbot_search! This MCP allows users to search for news results using advanced query capabilities. With the MCP, you can retrieve relevant news articles and information based on specific queries, and tailor the results based on user location and time sensitivity. This documentation outlines the available endpoint and its functionalities.

## Tool Overview

### 1. NBot Search

- **Name**: `nbot_search`
- **Description**: Search with NBot for news results.

#### Input Schema

- `query`: The query to search for NBot answers. (Type: string, Required)
- `zipcode`: The zipcode of the user conducting the search. Can be used to filter results based on location. (Type: string or null)
- `time_sensitive`: Indicates whether the answer is time-sensitive or not. (Type: boolean or null)
