
# Project Summary

## Project Overview

This project aims to develop a multilingual translation and speech recognition backend service. The service integrates the open-source `seamless_communication` model to support speech-to-speech, speech-to-text, text-to-speech, text-to-text translation, and automatic speech recognition (ASR). The project uses the Django framework for development and provides API endpoints via the REST framework.

## Key Features

1. **Speech-to-Speech Translation**
   - Input: Source audio file, translates it into target language audio file and text.
   - API Endpoint: `/m4t/s2st/`
   
2. **Speech-to-Text Translation**
   - Input: Source audio file, translates it into target language text.
   - API Endpoint: `/m4t/s2tt/`
   
3. **Text-to-Speech Translation**
   - Input: Source text, translates it into target language audio file and text.
   - API Endpoint: `/m4t/t2st/`
   
4. **Text-to-Text Translation**
   - Input: Source text, translates it into target language text.
   - API Endpoint: `/m4t/t2tt/`
   
5. **Automatic Speech Recognition (ASR)**
   - Input: Audio file, converts it into target language text.
   - API Endpoint: `/m4t/asr/`

## Development Environment Setup

1. **Create Virtual Environment and Install Dependencies**
   ```sh
   conda create --name diatrans38 python=3.8
   conda activate diatrans38
   pip install -r requirements.txt
   ```

2. **Start Django Server**
   ```sh
   python manage.py runserver
   ```

## Storage Strategy

Currently, the project uses a local storage strategy to store received audio files and processed files. In the future, cloud storage services (such as AWS S3) can be considered to improve storage and management efficiency.

Through this project, we have developed a comprehensive multilingual translation and speech recognition service that can be easily integrated into front-end applications, providing high-quality translation experiences.

## API Usage Guide

Below is a detailed description of each translation and speech recognition endpoint for front-end engineers to understand how to interact with the backend.

---

#### 1. Speech-to-Speech Translation

**Request URL**:
```
http://127.0.0.1:8000/m4t/s2st/
```

**Request Method**:
```
POST
```

**Request Parameters**:
- `input_audio`: The audio file to be translated (type: file).
- `source_language`: The name of the source language (type: string).
- `target_language`: The name of the target language (type: string).

**Example Request**:
When using Postman or other HTTP client tools, set as follows:
- **URL**: `http://127.0.0.1:8000/m4t/s2st/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_audio` | **Type**: `File`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**Response**:
```json
{
    "sample_rate": 16000,
    "output_audio": <audio data array>,
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 2. Speech-to-Text Translation

**Request URL**:
```
http://127.0.0.1:8000/m4t/s2tt/
```

**Request Method**:
```
POST
```

**Request Parameters**:
- `input_audio`: The audio file to be translated (type: file).
- `source_language`: The name of the source language (type: string).
- `target_language`: The name of the target language (type: string).

**Example Request**:
- **URL**: `http://127.0.0.1:8000/m4t/s2tt/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_audio` | **Type**: `File`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**Response**:
```json
{
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 3. Text-to-Speech Translation

**Request URL**:
```
http://127.0.0.1:8000/m4t/t2st/`
```

**Request Method**:
```
POST
```

**Request Parameters**:
- `input_text`: The text to be translated (type: string).
- `source_language`: The name of the source language (type: string).
- `target_language`: The name of the target language (type: string).

**Example Request**:
- **URL**: `http://127.0.0.1:8000/m4t/t2st/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_text` | **Type**: `Text` | **Value**: `Hello, how are you?`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**Response**:
```json
{
    "sample_rate": 16000,
    "output_audio": <audio data array>,
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 4. Text-to-Text Translation

**Request URL**:
```
http://127.0.0.1:8000/m4t/t2tt/`
```

**Request Method**:
```
POST
```

**Request Parameters**:
- `input_text`: The text to be translated (type: string).
- `source_language`: The name of the source language (type: string).
- `target_language`: The name of the target language (type: string).

**Example Request**:
- **URL**: `http://127.0.0.1:8000/m4t/t2tt/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_text` | **Type**: `Text` | **Value**: `Hello, how are you?`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**Response**:
```json
{
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 5. Automatic Speech Recognition (ASR)

**Request URL**:
```
http://127.0.0.1:8000/m4t/asr/`
```

**Request Method**:
```
POST
```

**Request Parameters**:
- `input_audio`: The audio file to be recognized (type: file).
- `target_language`: The name of the target language (type: string).

**Example Request**:
- **URL**: `http://127.0.0.1:8000/m4t/asr/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_audio` | **Type**: `File`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `English`

**Response**:
```json
{
    "output_text": "Hello, how are you?"
}
```

With these endpoints, front-end engineers can easily interact with the backend to perform various language translation and speech recognition tasks.
