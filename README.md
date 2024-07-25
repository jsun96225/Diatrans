
# API 接口使用指南

以下是各个翻译和语音识别接口的详细说明，前端工程师可以根据这些说明了解如何与后端进行交互。

---

#### 1. 语音到语音翻译 (Speech-to-Speech Translation)

**请求 URL**:
```
http://127.0.0.1:8000/m4t/s2st/
```

**请求方法**:
```
POST
```

**请求参数**:
- `input_audio`: 要翻译的语音文件（类型：文件）。
- `source_language`: 源语言的名称（类型：字符串）。
- `target_language`: 目标语言的名称（类型：字符串）。

**示例请求**:
使用 Postman 或其他 HTTP 客户端工具发送请求时，设置如下：
- **URL**: `http://127.0.0.1:8000/m4t/s2st/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_audio` | **Type**: `File`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**响应**:
```json
{
    "sample_rate": 16000,
    "output_audio": <音频数据数组>,
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 2. 语音到文本翻译 (Speech-to-Text Translation)

**请求 URL**:
```
http://127.0.0.1:8000/m4t/s2tt/
```

**请求方法**:
```
POST
```

**请求参数**:
- `input_audio`: 要翻译的语音文件（类型：文件）。
- `source_language`: 源语言的名称（类型：字符串）。
- `target_language`: 目标语言的名称（类型：字符串）。

**示例请求**:
- **URL**: `http://127.0.0.1:8000/m4t/s2tt/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_audio` | **Type**: `File`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**响应**:
```json
{
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 3. 文本到语音翻译 (Text-to-Speech Translation)

**请求 URL**:
```
http://127.0.0.1:8000/m4t/t2st/
```

**请求方法**:
```
POST
```

**请求参数**:
- `input_text`: 要翻译的文本（类型：字符串）。
- `source_language`: 源语言的名称（类型：字符串）。
- `target_language`: 目标语言的名称（类型：字符串）。

**示例请求**:
- **URL**: `http://127.0.0.1:8000/m4t/t2st/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_text` | **Type**: `Text` | **Value**: `Hello, how are you?`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**响应**:
```json
{
    "sample_rate": 16000,
    "output_audio": <音频数据数组>,
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 4. 文本到文本翻译 (Text-to-Text Translation)

**请求 URL**:
```
http://127.0.0.1:8000/m4t/t2tt/
```

**请求方法**:
```
POST
```

**请求参数**:
- `input_text`: 要翻译的文本（类型：字符串）。
- `source_language`: 源语言的名称（类型：字符串）。
- `target_language`: 目标语言的名称（类型：字符串）。

**示例请求**:
- **URL**: `http://127.0.0.1:8000/m4t/t2tt/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_text` | **Type**: `Text` | **Value**: `Hello, how are you?`
  - **Key**: `source_language` | **Type**: `Text` | **Value**: `English`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `French`

**响应**:
```json
{
    "output_text": "Bonjour, comment ça va ?"
}
```

---

#### 5. 自动语音识别 (Automatic Speech Recognition, ASR)

**请求 URL**:
```
http://127.0.0.1:8000/m4t/asr/
```

**请求方法**:
```
POST
```

**请求参数**:
- `input_audio`: 要识别的语音文件（类型：文件）。
- `target_language`: 目标语言的名称（类型：字符串）。

**示例请求**:
- **URL**: `http://127.0.0.1:8000/m4t/asr/`
- **Method**: `POST`
- **Body**: `form-data`
  - **Key**: `input_audio` | **Type**: `File`
  - **Key**: `target_language` | **Type**: `Text` | **Value**: `English`

**响应**:
```json
{
    "output_text": "Hello, how are you?"
}
```

通过以上接口，前端工程师可以方便地与后端进行交互，完成各种语言翻译和语音识别的任务。
