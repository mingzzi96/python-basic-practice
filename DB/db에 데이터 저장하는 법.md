# db에 저장하는 법 (터미널에 입력)

## 데이터를 DB에 저장하기

```py
song = Song(username="추천자", title="노래제목",
artist="가수", image_url="이미지 주소")
db.session.add(song)
db.session.commit()
```

## 모든 데이터 조회하기

```py
song_list = Song.query.all()
```

## 데이터 1개 가져오기

> first는 하나만 가져오겠다는 뜻

```py
Song.query.filter_by(id=3).first()
```

## 데이터 변경하기

```py
song_data = Song.query.filter_by(id=4).first()
song_data.title = '변경된제목'
db.session.add(song_data)
db.session.commit()
```

## 데이터 삭제하기

```py
delete_data = Song.query.filter_by(id=4).first()
db.session.delete(delete_data)
db.session.commit()
```
