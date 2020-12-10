from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/home')
def main():
    return render_template('homepage.html')

@app.route('/bmi')
def mainn():
    return render_template('bmi_cal.html')

@app.route('/bmr')
def mainnn():
    return render_template('bmr_cal.html')


@app.route("/bmi", methods=['POST'])#process_bmi
def bmi_cal():
    tips = ""
    bmi_ans = "กรุณากรอกข้อมูลให้ถูกต้อง"
    kg_bmi = request.form['kg_bmi_input']
    height_bmi = request.form['height_bmi_input']
    if kg_bmi.isdigit() and height_bmi.isdigit():
        bmi_ans = round(float(kg_bmi) / ((float(height_bmi)/100) ** 2), 2)
        if bmi_ans < 18.5:
            result = "คุณต้องเพิ่มค่าBMIอีก "+"%.2f" %(abs(bmi_ans-18.5))+" จึงจะมีค่า BMI ในระดับปกติ"
            kg_ans = float(abs(abs(18.5*((float(height_bmi)/100)**2))-float(kg_bmi)))
            secret = "***เคล็ดไม่ลับ คุณต้องเพื่มน้ำหนักอีก " +"%.2f" %(kg_ans)+" กิโลกรัม เพื่อให้ค่า BMI อยู่ในระดับปกติ***"
            tips = "น้ำหนักน้อย/ผอม"
        elif 18.5 <= bmi_ans <= 22.9:
            result = "ค่า BMI ของคุณอยู่ในระดับปกติแล้ว"
            kg_ans = float(abs(abs(22.9*((float(height_bmi)/100)**2))-float(kg_bmi)))
            secret = "***เคล็ดไม่ลับ รักษาค่านี้ไว้ให้คงอยู่ตลอดนะะ***"
            tips = "ปกติ"
        elif 23 <= bmi_ans <= 24.9:
            result = "คุณต้องลดค่าBMIอีก "+"%.2f" %(abs(bmi_ans-22.9))+" จึงจะมีค่า BMI ในระดับปกติ"
            kg_ans = float(abs(abs(22.9*((float(height_bmi)/100)**2))-float(kg_bmi)))
            secret = "***เคล็ดไม่ลับ คุณต้องลดน้ำหนักอีก " +"%.2f" %(kg_ans)+" กิโลกรัม เพื่อให้ค่า BMI อยู่ในระดับปกติ***"
            tips = "ท้วม/โรคอ้วนระดับ 1"
        elif 25 <= bmi_ans <= 29.9:
            result = "คุณต้องลดค่าBMIอีก "+"%.2f" %(abs(bmi_ans-22.9))+" จึงจะมีค่า BMI ในระดับปกติ"
            kg_ans = float(abs(abs(22.9*((float(height_bmi)/100)**2))-float(kg_bmi)))
            secret = "***เคล็ดไม่ลับ คุณต้องลดน้ำหนักอีก " +"%.2f" %(kg_ans)+" กิโลกรัม เพื่อให้ค่า BMI อยู่ในระดับปกติ***"
            tips = "ท้วม/โรคอ้วนระดับ 2"
        else:
            result = "คุณต้องลดค่าBMIอีก "+"%.2f" %(abs(bmi_ans-22.9))+" จึงจะมีค่า BMI ในระดับปกติ"
            kg_ans = float(abs(abs(22.9*((float(height_bmi)/100)**2))-float(kg_bmi)))
            secret = "***เคล็ดไม่ลับ คุณต้องลดน้ำหนักอีก " +"%.2f" %(kg_ans)+" กิโลกรัม เพื่อให้ค่า BMI อยู่ในระดับปกติ***"
            tips = "ท้วม/โรคอ้วนระดับ 3"
        return render_template('bmi_cal.html', bmi_ans=bmi_ans, tips=tips, result=result, secret=secret)
    else:
        return render_template('bmi_cal.html', bmi_ans=bmi_ans)



@app.route("/bmr", methods=["POST"])#process_bmr
def bmr_cal():
    bmr_ans = "กรุณากรอกข้อมูลให้ถูกต้อง"
    ans = ""
    kg_bmr = request.form['kg_bmr_input']
    height_bmr = request.form['height_bmr_input']
    age_bmr = request.form['age_bmr_input']
    sex_from_html = request.form['sex_bmr']
    if kg_bmr.isdigit() and height_bmr.isdigit():
        if sex_from_html == "male":
            bmr_ans = str(int(66 + (13.7*float(kg_bmr)) + (5*float(height_bmr)) - (6.8 * float(age_bmr))))+" Kcal"
            ans = "หมายความว่าในหนึ่งวัน ร่างกายจะเผาผลาญพลังงานทั้งหมด "+str(bmr_ans)+" (ไม่รวมกิจกรรมที่ทำในวันนั้น)"
            return render_template('bmr_cal.html', bmr_ans=bmr_ans, ans=ans)
        elif sex_from_html == "female":
            bmr_ans = str(int(665 + (9.6 * float(kg_bmr)) + (1.8 * float(height_bmr)) - (4.7 * float(age_bmr))))+" Kcal"
            ans = "หมายความว่าในหนึ่งวัน ร่างกายจะเผาผลาญพลังงานทั้งหมด "+str(bmr_ans)+" (ไม่รวมกิจกรรมที่ทำในวันนั้น)"
            return render_template('bmr_cal.html', bmr_ans=bmr_ans, ans=ans)
    else:
        return render_template('bmr_cal.html', bmr_ans=bmr_ans, ans=ans)



if __name__ == "__main__":
    app.run(debug=True)
