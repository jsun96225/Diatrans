from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .inference import run_s2st, run_s2tt, run_t2st, run_t2tt, run_asr
import os
import torchaudio

# 定义存储目录
UPLOADED_AUDIO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'uploaded_audio')
TRANSLATED_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'translated_files')
os.makedirs(UPLOADED_AUDIO_DIR, exist_ok=True)
os.makedirs(TRANSLATED_FILES_DIR, exist_ok=True)


@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def s2st(request):
    input_audio = request.FILES['input_audio']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    input_audio_path = os.path.join(UPLOADED_AUDIO_DIR, input_audio.name)
    with open(input_audio_path, 'wb+') as destination:
        for chunk in input_audio.chunks():
            destination.write(chunk)

    sample_rate, output_audio, output_text = run_s2st(input_audio_path, source_language, target_language)

    # 保存翻译结果
    output_audio_path = os.path.join(TRANSLATED_FILES_DIR, f'output_{input_audio.name}')
    torchaudio.save(output_audio_path, torch.tensor(output_audio).unsqueeze(0), sample_rate)

    return Response({
        'sample_rate': sample_rate,
        'output_audio_path': output_audio_path,
        'output_text': output_text
    })


@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def s2tt(request):
    input_audio = request.FILES['input_audio']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    input_audio_path = os.path.join(UPLOADED_AUDIO_DIR, input_audio.name)
    with open(input_audio_path, 'wb+') as destination:
        for chunk in input_audio.chunks():
            destination.write(chunk)

    output_text = run_s2tt(input_audio_path, source_language, target_language)

    return Response({'output_text': output_text})


@api_view(['POST'])
@permission_classes([AllowAny])
def t2st(request):
    input_text = request.data['input_text']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    sample_rate, output_audio, output_text = run_t2st(input_text, source_language, target_language)

    # 保存翻译结果
    output_audio_path = os.path.join(TRANSLATED_FILES_DIR, f'output_{input_text[:10]}.wav')
    torchaudio.save(output_audio_path, torch.tensor(output_audio).unsqueeze(0), sample_rate)

    return Response({
        'sample_rate': sample_rate,
        'output_audio_path': output_audio_path,
        'output_text': output_text
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def t2tt(request):
    input_text = request.data['input_text']
    source_language = request.data['source_language']
    target_language = request.data['target_language']
    output_text = run_t2tt(input_text, source_language, target_language)

    return Response({'output_text': output_text})


@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def asr(request):
    input_audio = request.FILES['input_audio']
    target_language = request.data['target_language']
    input_audio_path = os.path.join(UPLOADED_AUDIO_DIR, input_audio.name)
    with open(input_audio_path, 'wb+') as destination:
        for chunk in input_audio.chunks():
            destination.write(chunk)

    output_text = run_asr(input_audio_path, target_language)

    return Response({'output_text': output_text})
