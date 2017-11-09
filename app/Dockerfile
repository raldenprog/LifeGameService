FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# RUN ls api/
# RUN python api/database/add_table.py
CMD [ "python", "./main.py" ]
