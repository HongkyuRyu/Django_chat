# 가장 가까운 위치에 있는 관측소 반환하는 함수

def get_observation_code(x, y):
    import pandas as pd
    df = pd.read_csv(
        "C:\\Users\\minsu\\Documents\\ocearn\\Django_chat\\backend\\ocean\\data\\관측소.csv", encoding='utf-8')
    df["거리"] = ((df["위도"] - x)**2 + (df["경도"] - y)**2)**(1/2)
    df = df.sort_values(by="거리", ascending=True)
    return df.iloc[0, 0]
