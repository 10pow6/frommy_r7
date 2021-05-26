import requests
import itertools

base_url="https://forms.gle/"

#     aa%%A%AaA%aaAAAA%
#     aa %% A % A a A % aa AAAA %


#########################################################
##### Confirmed assumption that the legend is accurate
#########################################################
'''
#<aa> also q known q as q tzdata, p the p zone info q database q or p IANA q time q zone p database
p_1 = ["tz","zt"] #high confidence

#<%%> Earth Three
p_2 = ["34","43","35","53"]

#<A> Direct Message (w, Shane is reading) --- w upside down  
p_3 = ["M"]   

#<%> Piano
p_4 = ["8"] 

#<A> Girl Pointing to You
p_5 = ["U"]

#<a> x marks spot
p_6 = ["x"] 

#<A> double (paper clue)
# there is a possibility this clue laps over into another field resulting in A% here, ubuntu as an a, and mirror as an a
p_7 = ["A"] 

#<%> ubuntu new install
p_8 = ["0","1","7","8","9"] 

#<aa> d mirror
p_9 = ["db","bd"] #high confidence

#<AAAA> 12 words
p_10 = ["LIHI","LHBR"] 

#<%> eyeglasses
p_11 = ["0","2","8"] #high confidence
'''
#<aa> also q known q as q tzdata, p the p zone info q database q or p IANA q time q zone p database  {timezone database}
p_1 = ["tz"] #high confidence

#<%%> Earth Three
p_2 = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99"]

#<A> w, Shane is reading {w upside down is M; reference to meme of Australia being upside down}
p_3 = ["M"]  #high confidence

#<%> Piano {8 in an octave, regardless if keyboard, guitar, or flute}
p_4 = ["8"]  #high confidence

#<A> Girl Pointing to You {Thomas probably searched 'woman pointing at you'}
p_5 = ["U"] #high confidence

#<a> Treasure Map with x
p_6 = ["x"] #high confidence {x marks the spot}

#<A%> Paper sizes
# there is a possibility this clue laps over into another field resulting in A% here, ubuntu as an a, and mirror as an a
p_7 = ["A2","A3","A4","A5","A7"] 

#<a> ubuntu new install
p_8 = ["y"] 

#<a> d mirror 
# either d or b -- mirroring of the letter
p_9 = ["d","b"] #high confidence

#<AAAA> Later I will go to the Hotel and I will bring rubies. {capital letters??}
p_10 = ["LIHI"] 

#<%> eyeglasses {they look like an 8}
p_11 = ["0","8"] #high confidence


a = [ p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11 ]

result = list(itertools.product(*a))
print( "Total Possible Combos: ", len(result) )

f = open("exclusions.txt", "r+")
q = open("investigate_manually.txt", "r+")

exclusions = f.read().splitlines() 
#print(exclusions)

# Test URL Format
'''
for url_id in result:
    parsed = url_id[0] + url_id[1] + url_id[2] + url_id[3] + url_id[4] + url_id[5] + url_id[6] + url_id[7] + url_id[8] + url_id[9] + url_id[10]
    print(parsed)
'''

# Test Valid versus Invalid Form Link Status Code
'''
a = requests.get("https://forms.gle/q4evpmuRUBMdG7bS6")
print("Status (Working): ", a.status_code)
a = requests.get("https://forms.gle/tze3W0UxA8dbLIHI2")
print("Status (Bad): ", a.status_code)
'''


# Execute Requests
for count,url_id in enumerate(result):
    parsed = url_id[0] + url_id[1] + url_id[2] + url_id[3] + url_id[4] + url_id[5] + url_id[6] + url_id[7] + url_id[8] + url_id[9] + url_id[10]

    if parsed not in exclusions:
        exclusions.append(parsed)

        new_url = base_url + parsed
        #print(new_url)
        

        try:
            a = requests.get(new_url)

            line = str(count) + "," + parsed + "," + new_url + "," + str(a.status_code)

            if a.status_code == 200:
                line = line + ",BINGO"
                print(line)
                break
            elif a.status_code == 404:
                line = line + ",FAILED"
                print(line)
                f.write( parsed )
                f.write( "\n" )
            else:
                line = line + ",UNEXPECTED"
                print(line)
                q.write(line)
                q.write("\n")
        except KeyboardInterrupt:
            print("Broke @ ", parsed)
            break
        except Exception as e:
            new_url = base_url + parsed
            line = str(count) + "," + parsed + "," + new_url + ",N/A,ERROR"
            print(line)
    else:
        new_url = base_url + parsed
        line = str(count) + "," + parsed + "," + new_url + ",N/A,SKIPPED"
        print(line)

q.close()
f.close()
