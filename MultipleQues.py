import random
question = [{"q": "Who is the prime minister of India?", "a": "Narendra Modi", "b": "Nitish Kumar", "c":"Amit Shah", "d": "Rajnath Singh", "ans": "a"}, {"q": "Which state reports first confirmed coronavirus case in India", "a": "Odisha", "b": "Punjab", "c": "Goa", "d": "Kerala", "ans": "d"}, {"q": "How many keyword C has?", "a":"23", "b": "45", "c": "28", "d": "32", "ans": "d"}, {"q": "DOS is a ", "a": "Application Software", "b": "Operating System", "c": "Antivirus", "d": "None of these", "ans": "b"},
            {"q": "When is the World Aids Day observed every year?", "a": "December 1", "b": "December 5", "c": "December 10", "d": "December 15", "ans": "a"}, {"q": "Which country is the first in the world to permit the sale of lab grown meat?", "a": "China", "b": "Japan", "c": "Sinapore", "d": "Russia", "ans": "c"}, {"q": "----- Won Ballon d'Or award 2019", "a": "Neymar", "b": "Virgil van Dijk", "c": "Cristiano Ronado", "d": "Lionel Messi", "ans": "d"},
            {"q": "India has been listed at the rank of__in Geo-political Risk list of 2020", "a": "1st", "b": "10th", "c": "5th", "d": "6th", "ans": "c"}, {"q": "Amma Vodi scheme was launched by state ______", "a": "Assam", "b": "Arunachal Pradesh", "c": "Odisha", "d": "Anhra Pradesh", "ans": "d"},
            {"q": "United Nations Lowered India's growth forecast for FY20 to ___", "a": "7.1%", "b": "6.2%", "c": "5.7", "d": "5.8%", "ans": "c"},
            {"q": "Naseem-Al-Bahr is a bilateral navel exercise between India and-", "a": "United Arab Emirates", "b": "Iran", "c": "Saudi Arebia", "d": "Oman", "ans": "d"}, {"q": "Till when does the government want to eliminate the Tuberculoris?", "a": "2030", "b": "2027", "c": "2025", "d": "2022", "ans": "c"}, {"q": "The first floating solar power plant in Utter Pradesh is built on which of the following dams?", "a": "Matatila Dam", "b": "Rajghat Dam", "c": "Dhanraul Dam", "d": "Rihand Dam", "ans": "d"}]
qntba = {random.randint(0, len(question))}
maxQuestion = 5
while len(qntba) < maxQuestion:
    qntba.add(random.randint(0, len(question)))
ans =[]
qntba = list(qntba)
for i in range(0, maxQuestion):
    print(question[qntba[i]]["q"])
    print(question[qntba[i]]["a"])
    print(question[qntba[i]]["b"])
    print(question[qntba[i]]["c"])
    print(question[qntba[i]]["d"])
    uans = input("Enter answer:")
    d = {}
    d["qn"] = qntba[i]
    d["ans"] = uans
    ans.append(d)

print(ans)




