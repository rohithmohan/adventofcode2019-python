# Grab Advent of Code input data
# Reads in cookie session id from sessionid_file, change as needed

import os
import argparse
import datetime

try:
    import requests
except ImportError:
    raise ImportError('Requests module is missing, please install using pip.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", help="Advent of Code Day Input")
    parser.add_argument("--year", help="Advent of Code Year Input")
    args = parser.parse_args()
    if args.day:
        day_id = str(args.day)
    else:
        day_id = str(datetime.datetime.today().day)

    if args.year:
        year_id = str(args.year)
    else:
        year_id = str(datetime.datetime.today().year)

    base_dir = "./"
    max_connection_attempts = 2
    year_id = "2019"
    sessionid_file = "./sessionid"

    with open(sessionid_file, 'r') as sessionid_fh:
        sessionid = sessionid_fh.read().replace('\n', '')

    if not os.path.exists(base_dir + "Day " + str(day_id)):
        os.mkdir(base_dir + "Day " + str(day_id))
    else:
        print("Directory for Day " + str(day_id) + " already exists.")

    if not os.path.exists(base_dir + "Day " + str(day_id) + "/input.txt"):
        print("Grabbing input data from https://adventofcode.com/day/" +
              str(day_id) + "/input")
        endOfRequestFlag = False
        numErrors = 0
        while (not endOfRequestFlag):
            try:
                response = requests.get(
                    url="https://adventofcode.com/" + str(year_id) + "/day/" +
                    str(day_id) + "/input",
                    cookies={"session": sessionid},
                    headers={"User-Agent": "AoC_inputdata_request"})
                if response.ok:
                    data = response.text
                    input = open(base_dir + "Day " + day_id + "/input.txt",
                                 "w+")
                    input.write(data.rstrip("\n"))
                    input.close()
                    print("Finished grabbing data! \U0001f600")
                else:
                    print(
                        str(response.status_code) +
                        " status code encountered.")
                endOfRequestFlag = True
            except requests.exceptions.RequestException:
                numErrors += 1
                if numErrors > max_connection_attempts:
                    print("Max connection attempts reached, exiting.")
                    endOfRequestFlag = True
                else:
                    print(
                        "Couldn't get input data from Advent of Code website.",
                        "Trying again.")
            except Exception as e:
                print(str(e))
                endOfRequestFlag = True
    else:
        print("input.txt for Day " + str(day_id) + " already exists.")
