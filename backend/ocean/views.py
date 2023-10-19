from rest_framework.views import APIView
from rest_framework.response import Response
from secret import *
import requests


class ObservationView(APIView):
    def get(self, request):
        obs_code = request.GET.get('ObsCode')
        date = request.GET.get('Date')

        # 유효성 검사
        if not obs_code or not date:
            return Response({'error': '관측소 정보와 날짜 정보가 필요합니다.'}, status=400)

        service_key = SOCIAL_INFO['OCEAN_SECRET_KEY']

        if not service_key:
            return Response({'error': 'Service key not found'}, status=500)

        try:
            # API 호출 및 데이터 가져오기
            api_url = f'http://www.khoa.go.kr/api/oceangrid/DataType/search.do?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType=json'
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:
            return Response({'error': 'API request failed'}, status=500)
