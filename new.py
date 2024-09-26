def calculate_bmi(weight, height):
    # 身高需要轉換為公尺
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

weight = float(input("請輸入您的體重 (公斤): "))
height = float(input("請輸入您的身高 (公分): "))

bmi = calculate_bmi(weight, height)

print("您的 BMI 是: ", bmi)
