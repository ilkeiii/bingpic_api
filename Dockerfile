FROM python:3.12.0-alpine3.18
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests et flask
WORKDIR /app/
COPY bing_pic_api.py .
EXPOSE 8080
CMD [ "python3","bing_pic_api.py" ]