import csv
import json
import pprint
import sys
import urllib2

# load config settings
config = json.load(open('config.json'))
apiUrl = "https://api.github.com/repos/" + config['username'] + "/" + config[
    'repoName'] + "/stats/contributors?access_token=" + config['accessToken']


def by_week():
    """Get week-to-week burndown data"""

    # program defaults
    outputFile = "budo_results.csv"
    hoursMultiplier = 0.005
    startWeek = 0
    endWeek = -1

    if len(sys.argv) > 1:
        outputFile = sys.argv[1]
    if len(sys.argv) > 2:
        hoursMultiplier = float(sys.argv[2])
    if len(sys.argv) > 3:
        startWeek = int(sys.argv[3])
    if len(sys.argv) > 4:
        endWeek = int(sys.argv[4])

    # headings for output
    outputData = [[
        "total # of weeks",
        "additions",
        "deletions",
        "total adds and dels",
        "work hours multiplier",
        "estimated total work hours"
    ]]

    try:
        # get repository data
        response = urllib2.urlopen(apiUrl)
        jd = json.load(response)

        # gather specified data from our incoming results
        for i in range(0, len(jd[0]["weeks"])):
            if (jd[0]["weeks"][i]['w'] >= startWeek and jd[
                    0]["weeks"][i]['w'] <= endWeek) or (endWeek < 0):
                outputData.append(
                    [
                        jd[0]["weeks"][i]['w'],
                        jd[0]["weeks"][i]["a"],
                        jd[0]["weeks"][i]["d"],
                        jd[0]["weeks"][i]["a"] +
                        jd[0]["weeks"][i]["d"],
                        hoursMultiplier,
                        (jd[0]["weeks"][i]["a"] +
                         jd[0]["weeks"][i]["d"]) *
                        hoursMultiplier])

        # save results to output file
        output = csv.writer(open(outputFile, 'wb'), delimiter=",")
        for line in outputData:
            output.writerow(line)
    except urllib2.HTTPError, e:
        print "There was an HTTPError: " + str(e.code) + ".\nIs your `config.json` file set up?"
    except urllib2.URLError, e:
        print "There was a URLError: " + str(e.reason) + ".\nDid something happen to your `apiUrl` variable?"
    except:
        print "Sorry, there was an error..."

if __name__ == '__main__':
    by_week()
