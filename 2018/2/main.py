import collections
import difflib
inputs = ["tqzvwnogbarflkpcbdewsmjhxi","tqyvunogzarfckpcbdewsmzhci","tqyvunojzarflkpcbdcwsmyhxi","tqyvunogzarclkpcbdewmmjrxi","hqyvunogzarflkpcbczwsmjhxi","tqyvunogzarflppcudewsmjhei","tqrvunogzarflkpcbpewsmjhdi","aqyvunogzarflkpcbdewsjjsxi","tqyvtnogzarflkkcbdewymjhxi","tcyeunogzarfkkpcbdewsmjhxi","tqyvunozzarfvkpcbdewsqjhxi","tkyvuwjgzarflkpcbdewsmjhxi","tqevunogzarflkpnbdkwsmjhxi","tqyvunogqarflkpcppewsmjhxi","tqyvunsgzarflkpcbrewsmjhxk","tqyvunogzarffkpdbnewsmjhxi","tqyvunogvarflkpjbdewsojhxi","tqyvgnogzarflkpfbdswsmjhxi","tqyvunogzarfxkpcbtersmjhxi","tqyvukhgzarflupcbdewsmjhxi","tqyvdnoozyrflkpcbdewsmjhxi","tqyvunogzorflkpcbdewsvjhxd","tqyvunzqzarflkpcbdewxmjhxi","tqykunogzarulkpcbdhwsmjhxi","tqycdnogzarflkpcbdewsmjhxz","eqyvunogzarflkpcbdhwqmjhxi","cqyvunogzaralkpcbdewsmjvxi","vqyvunogzarflklcbeewsmjhxi","tqyvunogzarffkpcqdewlmjhxi","eqyvunogzarflkpcbdejsmahxi","tqyvunogjarflkocsdewsmjhxi","tqzvunogzanflkpcbdewsmjhxg","tqycunogzarflkpabdewsmkhxi","tqyvunogzarnlkpcbdewimjaxi","tqyvunogzarfzkpcbdepsyjhxi","gqykunogzarelkpcbdewsmjhxi","tqyvuwogzarflkpcbdrwsmjmxi","tqdqunogzarflkpcbdewsvjhxi","tqmvunbgzarflkpcbdewsvjhxi","tqyvunogzarflkpcbheesmjhdi","tqxvunogzarfxkpcbdewsmhhxi","tqyvunogzarflkpabdjosmjhxi","tqyvugogztrflkpybdewsmjhxi","tqyvundgzarflkxcbdewsmjhmi","tqyvunogzurfgkpcbdeksmjhxi","tqyvunokzarfckpcbdewsojhxi","tqyvufobzarflkpcldewsmjhxi","tqyvunogznrflkncbdeusmjhxi","tqyvuncgzarfxkpcmdewsmjhxi","oqyvunogzarflkpybdewbmjhxi","tqyvjnogqarfmkpcbdewsmjhxi","tqyvunogzacflkpcidewsmjhwi","tqyvunogzarflkpcbqlwxmjhxi","tqyvunogzarflkpnbhewsvjhxi","vqyiunogzarflkpcbdewsmjhqi","tbyvuncgzarfljpcbdewsmjhxi","tqylunogzarflkpcldexsmjhxi","tqyvulogzarflktcbdewsxjhxi","tqyvmnlgzarflkpcbxewsmjhxi","tqyvunogzartlkpcbdewsmihxp","nqyvunogzarflkpcbdewsmnwxi","tqyvunogzarflkpczdewsmjcxj","tzyvunogzariwkpcbdewsmjhxi","tqyiufogzarflipcbdewsmjhxi","oqyvunogzasflkpcbdewsmjhxv","tqyvunoqmarflkpcwdewsmjhxi","tqrvunogzarflkpqbdewnmjhxi","tqyvunogzarmlkocbdewsmjhri","tqyvunogzakflkpcbveasmjhxi","tqyvunorearflkpcbdewsmfhxi","tqynrnogzarflkpcbdewsmjhxp","tiyvueogzaeflkpcbdewsmjhxi","tqyrunogzarflkpccdewbmjhxi","tqtvunogzarflkpcbdewbnjhxi","tqyvfnogzarflhpcbdewsmjqxi","tqyjunoazarflkpcbdewssjhxi","tqyvunxizarflkpcbdewsmjnxi","tqyvunogzarfhkpobdewsmjhai","tqyaunogzanflkpcbxewsmjhxi","tqyvunogzarflkpsbuewsmjmxi","tqyvunogzarzlkwybdewsmjhxi","tqyvunogzarflkpibdawsmhhxi","tqyvunogzarflkycbdewamjwxi","tqyvunourarflkpcbdewsujhxi","tqyvnnogzirflkpcbdewsdjhxi","tayvunogzauflkpcqdewsmjhxi","tqyvunobzfrflkscbdewsmjhxi","tqygvnogzarflkpcbdewsmjnxi","oqyvunogzarflkpcbdewsmjsgi","tqyvunokzarflkpcbdewshjhii","tqyvunobzarflkvcbdewskjhxi","aqyvunogvarflkpcbdlwsmjhxi","tqyvunogzmrrlbpcbdewsmjhxi","tqyvunggzaqolkpcbdewsmjhxi","tqyvunogqarflkpybdewsmjaxi","tqyvunogzxrflkpcxsewsmjhxi","zqyvunogzarflppcbdewsmjhni","tqvvunogzakslkpcbdewsmjhxi","tqyrunogzarzlkpcbdewsmjtxi","tqyvhnogzarfxkpcbdewqmjhxi","tqyvunogzarflkecbdewgdjhxi","tqyvuwogzerfhkpcbdewsmjhxi","tqmvunogzarflkpcbddwsmdhxi","tqyvunogzarflcqcbdewsmihxi","tqyvunogzarvlkpcbdewsmjmxd","tqyvknogzarfllncbdewsmjhxi","tqyvunogzarflbpcbdrwsajhxi","tqyvunogzarfukpcbddwsmjhii","tqyvuvojzahflkpcbdewsmjhxi","tqyvunogzarfchpcbdeqsmjhxi","wqivueogzarflkpcbdewsmjhxi","tqyvunogzwrflkpcbdewstjhxz","tqyvunogzarfloscbdewsmjhxf","tqfbuiogzarflkpcbdewsmjhxi","tqyvfuogzarflkpcxdewsmjhxi","tqyvunogzarflkpcpdewsmgqxi","tqyvunogzdrflkpcbdewsmqhci","tqyvunogzartlkpcbdewsmjpxj","tqyfunogzarfwkpcbdewsmwhxi","tqyvuntgzarflkjcmdewsmjhxi","tqyvunqfzarflkpckdewsmjhxi","nqyvunogznrflkpcbiewsmjhxi","tqymunobzarflkccbdewsmjhxi","tqyvunogzaoflkprbdewzmjhxi","tqyvunogzaiflkpcvdewbmjhxi","tqwvunogzarfzkpcbdewsmjhxx","txhvunogzarflkpcbdewsijhxi","tqyeunogkarflkicbdewsmjhxi","tqylunogzarylkpcbdewsmkhxi","tqyvriogzarflkpcbdewsmohxi","tqyvunogzsrflkpcbdeasijhxi","tqyvunogzarflkpcbfewcmjhxh","tqyvunoozvrflkpcbdewimjhxi","tqyvunogqayflkpcidewsmjhxi","tqyounogzarflkpccdewsmjhxg","tqgvunogsarflkpcbdewqmjhxi","tqevunogzarflkpcbmewsmjhpi","tqivunogzarflkgcbdewqmjhxi","tqyuunogzlrflkgcbdewsmjhxi","xqyvbnogznrflkpcbdewsmjhxi","tqyvunogzarfjkpebdewsmnhxi","tqyvvnogzarfskpcxdewsmjhxi","thovunogzarflkpcbdewsmjhvi","tqyvunugzarflkpcpdewsmjrxi","tcyvvnogzarflkdcbdewsmjhxi","tqdfunogzarflkpbbdewsmjhxi","tqyvunogzarflkpcbdnwsejzxi","tqyvunivkarflkpcbdewsmjhxi","tqyvunogzawflopcbdewsmjhmi","tqyvunogzarflkpcbdkwsdjqxi","tqyvunodzarflkpcbdewlmjhei","oqyvunoozarflkpcbdemsmjhxi","tiyvunogzarjlkpcbdewfmjhxi","tqrvunogearflkpcbdewsojhxi","tqyvunkgzarflkpcbdcwtmjhxi","tqmvunogzarflkpcbdpwsmjtxi","tqyvunogzarflkpcydeptmjhxi","tqyvunkglarflkpcbdfwsmjhxi","tqyaunogzarflkpcbzeesmjhxi","tqyvunogzarrlkpcbdkwsmjhui","tpyvunogzarflkqcbdewsmjhxd","tvyvunogzarfkkpcbdewsajhxi","gqynunogzarflepcbdewsmjhxi","zqvvunogzarflkpcbdexsmjhxi","tqyyunogzawflkpcbdewsmjhxw","tfyvunogzarflkpcbdewomjrxi","tqyeunogzvrflrpcbdewsmjhxi","nqyvunogzarftkpabdewsmjhxi","tzyvunogzariwkpcbdewmmjhxi","tiyvunogzarflkpcbbewsmjhxa","tqydujoyzarflkpcbdewsmjhxi","tqyvunpgzarflkpcbdeysmjhwi","tqyvunogvarllkpcbdewsmshxi","tqyvunogzbrvlkpcbdewsmjhxp","tcyvueogzarflkacbdewsmjhxi","tqyvunogzrhflkpcbdetsmjhxi","tqavunogzrdflkpcbdewsmjhxi","tqyvunogzjrflkpcbdewstjhki","tqyqunolzarflkpcbdewbmjhxi","tqyvunogzarflkqczdgwsmjhxi","tqyvunogzqrfrkpcbrewsmjhxi","tqyvcnogzhrflkacbdewsmjhxi","tqyvunogzarflkpcbdewsmdhtk","tqyvunoggarftkpcbjewsmjhxi","tvyvunogzarfkkpcpdewsmjhxi","tqyvunogzawflkpcndedsmjhxi","tqyvunogzrrflkpcbdemsmmhxi","tqyvunogzarclkpcbrpwsmjhxi","tryvunogztrflkpcbbewsmjhxi","cqyvundgzarflkpcbdewgmjhxi","tqyvunogzarflktcbkewsmjqxi","tqyvjuogzarflkpcadewsmjhxi","tqyvunogzyrflkpcbbxwsmjhxi","ttyvunogzarflkpcbdewsnmhxi","tqyvunogzarflkpcbdeqsmlhki","fqyvugogzarflapcbdewsmjhxi","tqyvunogzartlkppbdewszjhxi","tqyvunfgztrflzpcbdewsmjhxi","tqyvunogmazflkpcbdewsmjhki","tqyvunzdzarflkpcbdewsmjhvi","tqyvunogzarflkpqbzewsujhxi","tqyvunogzarzlkpcbeewymjhxi","tqyounogzarflkpcbdewsnwhxi","tqysunogsaiflkpcbdewsmjhxi","tqdvunogdarflkpcboewsmjhxi","teyvunogzarflkscbdfwsmjhxi","tqyvunoazarflkpcbdvwsmjhpi","tqyvunooearflkpcbdewrmjhxi","tqyvunoszarflnrcbdewsmjhxi","tqyvunogzalflkpcblewsjjhxi","uqlvunkgzarflkpcbdewsmjhxi","tqyvunobzarflkpcidewsmjhvi","tnyvunogzarflkpcbdnwamjhxi","tqyoudogzarflkpcbdgwsmjhxi","tqyvunoggarflkpcbmewsmwhxi","tqykunogzazflkpcbddwsmjhxi","tfyvunogzarflkpcbdewsmjhgo","tqyvunogztrflkpcbdewoojhxi","tqyvunogzarflkpcbdewbmjoni","tmyvunogzalflkpabdewsmjhxi","tqyvunogzarflkpbbvewqmjhxi","tqyvunofzarflkpcwdexsmjhxi","tayvunogzasflkpcbdewsmhhxi","tqyvlnogzarflkpcbdewsmjwxd","tvyvunogzarflkpcbdewhmjrxi","tqyvunogzarplkpcsdewsmihxi","tqyvunogzarplklcbdewsmjtxi","rqbvunogzarhlkpcbdewsmjhxi","tqyvuxogzarftkpcbdewsmthxi","tqtvunogzarfikpczdewsmjhxi","tqyvunwgzarflkpcbdewsmjxxk","tqygunogzarzlkpnbdewsmjhxi","tqyvunogzarjlkpcbdbwswjhxi","tqyvunogzalfnkpcbdewsmjhxf","tqyucuogzarflkpcbdewsmjhxi","tzyvunogzvrflkpcbdewsmjaxi","tjyvunlgzarflkpcbdewgmjhxi","tqyvcnogzarklkpcbdewsmjhfi","tqyvunogzaaflkpsbaewsmjhxi","tsyvunogzarflkpctdewsmbhxi","tqyeunbgzarflkpcbdewrmjhxi","tqyvunogzcrflqpcbdeismjhxi","eqylunogzarflkpcbdewsmjhxy","tqyvundgzarflkpcbdewmmnhxi","tzyvunogzarflkpcndewsmjhxb","tkyvunogzxrflkpcbdewfmjhxi","tqyvunogzarflkxcbdzwsmjfxi","kqavunogzarflkycbdewsmjhxi","tqyvunogzarjlkpcbdxwkmjhxi","tqyvinogzarfqkpcbdewsmjpxi"]


def checksum():
    twos = 0
    threes = 0
    for i in inputs:
        letters = collections.Counter()
        for l in i:
            letters[l] += 1
        has_twos, has_threes = False, False
        for k, v in letters.items():
            if v == 2:
                has_twos = True
            if v == 3:
                has_threes = True
        if has_twos:
            twos += 1
        if has_threes:
            threes += 1
    print(twos, threes)
    print(twos * threes)

def matching():
    for a in inputs:
        for b in inputs:
            count = -1
            for i in range(len(a)):
                if a[i] != b[i]:
                    if count != -1:
                        count = -1 
                        break
                    count = i
            if count != -1:
                print(a[:count]+a[count+1:], b[:count]+b[count+1:])
                return



matching()
