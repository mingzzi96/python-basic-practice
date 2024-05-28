from flask import Flask, render_template
import random

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

if __name__ == '__main__':  
    app.run(debug=True)