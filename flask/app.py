from flask import Flask, render_template, request
from datetime import datetime, timedelta
import random
import requests

app = Flask(__name__)

@app.route('/')
def home():
    name = '권지밍'
    lotto = [16, 22, 20, 21, 3, 11]

    def generate_lotto_numbers():
        # 1에서 45까지의 숫자 중에서 6개를 랜덤으로 추첨
        numbers = random.sample(range(1, 46), 6)
        # 숫자를 오름차순으로 정렬
        numbers.sort()
        return numbers

    # 로또 번호 생성
    random_lotto = generate_lotto_numbers()

    def count_common_elements(list1, list2):
        # 두 리스트에서 공통된 요소를 찾기 위해 집합(set)을 사용합니다.
        set1 = set(list1)
        set2 = set(list2)
        
        # 두 집합의 교집합을 구하고 그 길이를 반환합니다.
        common_elements = set1.intersection(set2)
        return len(common_elements)

    # 공통된 요소의 개수를 출력합니다.
    common_count = count_common_elements(lotto, random_lotto)

    context= {
        "name" : name,
        "lotto" : lotto,
        "random_lotto": random_lotto,
        "common_count" : common_count,
    }
    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():
    return 'This is mypage!'

@app.route('/movie')
def movie():
    query = request.args.get('query')

    URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}"
    res = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    print(movie_list)
    return render_template('movie.html', data=movie_list)

@app.route("/boxoffice")
def boxoffice():
    # 현재 날짜에서 7일 전 날짜를 계산
    seven_days_ago = datetime.now() - timedelta(days=7)
    default_query = seven_days_ago.strftime('%Y%m%d')

    if request.args.get('query'):
        query = request.args.get('query')
    else:
        query = default_query

    URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={query}"

    res = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})

    rjson = res.json()
    movie_list = rjson.get("boxOfficeResult").get("weeklyBoxOfficeList")

    return render_template("boxoffice.html", data=movie_list)

if __name__ == '__main__':  
    app.run(debug=True)

    