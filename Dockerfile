FROM python

COPY . .

RUN pip install -r requirements.txt

#RUN python -m alembic upgrade head

CMD uvicorn src.main:app --0.0.0.0 --port 80