import requests
import json

def searchAndReplace(file, searchWord, replaceWord):
    with open(file, 'r', encoding="utf-8") as f:
        fileContents = f.read()
        f.close()

        updatedContents = fileContents.replace(searchWord, replaceWord)

    with open(file, 'w', encoding="utf-8") as f:
        f.write(updatedContents)
        f.close()


def main():
    # api-endpoint
    URL = "https://search.imdbot.workers.dev/"
    imdbNumber = 68646

    imdbIdList = ["imdb-id"]
    titleList = ["title"]
    descriptionList = ["description"]
    ratingList = ["rating"]
    contentRatingList = ["content rating"]
    genresList = ["genres"]
    actorsList = ["actors"]
    charactorsList = ["characters"]
    directorsList = ["directors"]
    creatorsList = ["creators"]
    releaseYearList = ["release year"]
    runTimeList = ["runtime"]
    AKAsList = ["AKAs"]
    countriesIDList = ["country ids"]
    countriesList = ["countries"]
    languagesList = ["languages"]
    keywordsList = ["keywords"]
    numberOfReviewsList = ["number of reviews"]

    for i in range(75):
        imdbNumber = imdbNumber + i
        imdbId = "tt00" + str(imdbNumber)
        PARAMS = {'tt': imdbId}
        r = requests.get(url=URL, params=PARAMS)
        data = json.loads(json.dumps(r.json(), indent=4))

        try:
            titleList.append(data["short"]["name"])
        except:
            titleList.append("")

        try:
            descriptionList.append(data["short"]["description"])
        except:
            descriptionList.append("No description given")

        try:
            imdbIdList.append(data["imdbId"])
        except:
            imdbIdList.append("")

        try:
            ratingList.append(str(data["short"]["aggregateRating"]["ratingValue"]))
        except:
            ratingList.append("No ratings given")

        try:
            contentRatingList.append(data["short"]["contentRating"])
        except:
            contentRatingList.append("No content rating given")

        try:
            appendString = ""
            for e in data["short"]["genre"]:
                appendString += e + ","

            genresList.append(appendString[:-1])
        except:
            genresList.append("No genres given")

        try:
            appendString1 = ""
            appendString2 = ""
            for e in data["main"]["cast"]["edges"]:
                appendString1 += e["node"]["name"]["nameText"]["text"] + ","

                for el in e["node"]["characters"]:
                    appendString2 += el["name"] + ","

            actorsList.append(appendString1[:-1])
            charactorsList.append(appendString2[:-1])
        except:
            actorsList.append("No actors given")
            charactorsList.append("No characters given")

        try:
            appendString = ""
            for e in data["short"]["director"]:
                appendString += e["name"] + ","

            directorsList.append(appendString[:-1])
        except:
            directorsList.append("No directors given")

        try:
            appendString = ""
            for e in data["short"]["creator"]:
                try:
                    appendString += e["name"] + ","
                except:
                    continue

            creatorsList.append(appendString[:-1])
        except:
            creatorsList.append("No creators given")

        try:
            releaseYearList.append(str(data["top"]["releaseYear"]["year"]))
        except:
            releaseYearList.append("No release year given")

        try:
            runTimeList.append(data["top"]["runtime"]["displayableProperty"]["value"]["plainText"])
        except:
            runTimeList.append("No runtime given")

        try:
            appendString = ""
            for e in data["main"]["akas"]["edges"]:
                appendString += e["node"]["text"] + ","

            AKAsList.append(appendString[:-1])
        except:
            AKAsList.append("No AKAs given")

        try:
            appendString = ""
            for e in data["main"]["countriesOfOrigin"]["countries"]:
                appendString += e["id"] + ","

            countriesIDList.append(appendString[:-1])
        except:
            countriesIDList.append("No countries given")

        try:
            appendString = ""
            for e in data["main"]["countriesOfOrigin"]["countries"]:
                appendString += e["text"] + ","

            countriesList.append(appendString[:-1])
        except:
            countriesList.append("No countries given")

        try:
            appendString = ""
            for e in data["main"]["spokenLanguages"]["spokenLanguages"]:
                appendString += e["text"] + ","

            languagesList.append(appendString[:-1])
        except:
            languagesList.append("No languages given")

        try:
            appendString = ""
            for e in data["top"]["keywords"]["edges"]:
                appendString += e["node"]["text"] + ","

            keywordsList.append(appendString[:-1])
        except:
            keywordsList.append("No keywords given")

        try:
            numberOfReviewsList.append(str(data["top"]["reviews"]["total"]))
        except:
            numberOfReviewsList.append("0")

    for i in range(len(titleList)):
        f = open("data.txt", "a", encoding="utf-8")
        result = "\""+imdbIdList[i]+"\""
        result+= ","
        result+="\""+titleList[i]+"\""
        result+=","
        result+="\""+ descriptionList[i]+"\""
        result+=","
        result+="\""+ratingList[i]+"\""
        result+=","
        result+="\""+contentRatingList[i]+"\""
        result+=","
        result+="\""+str(genresList[i])+"\""
        result+=","
        result+="\""+str(actorsList[i])+"\""
        result+=","
        result+="\""+str(charactorsList[i])+"\""
        result+=","
        result+="\""+str(directorsList[i])+"\""
        result+=","
        result+="\""+str(creatorsList[i])+"\""
        result+=","
        result+="\""+releaseYearList[i]+"\""
        result+=","
        result+="\""+runTimeList[i]+"\""
        result+=","
        result+="\""+str(AKAsList[i])+"\""
        result+=","
        result+="\""+str(countriesIDList[i])+"\""
        result+=","
        result+="\""+str(countriesList[i])+"\""
        result+=","
        result+="\""+str(languagesList[i])+"\""
        result+=","
        result+="\""+str(keywordsList[i])+"\""
        result+=","
        result+="\""+numberOfReviewsList[i]+"\""

        f.write(result + "\n")
        f.close()

    searchAndReplace("data.txt", "&apos;", "\'")
    searchAndReplace("data.txt", "&quot;", "\'")
    searchAndReplace("data.txt", "&amp;", "&")





if __name__ == "__main__":
    main()
