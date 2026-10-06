def cal_propinas(v_cuenta, p_propina=10):
    return v_cuenta * (p_propina/100)
print(cal_propinas(180000))
print(cal_propinas(180000,15))
