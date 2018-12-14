import sys
import requests


def main():
    title = " ".join(sys.argv[1:len(sys.argv)])

    session = requests.Session()

    response = session.get("http://www.omdbapi.com/", params={'apikey': "1d574033", 't': title})
    api_result = response.json()
    if 'Error' in api_result:
        sys.stderr.write("Error returned from API for title '%s': %s\n" % (title, api_result['Error']))
        sys.exit(1)

    if 'Ratings' not in api_result:
        sys.stderr.write("No ratings found for title '%s'\n" % title)
        sys.exit(1)

    rated = None
    for r in api_result['Ratings']:
        if "Rotten Tomatoes" == r['Source']:
            rated = r['Value']
            break

    if rated:
        print("The Rotten Tomatoes rating for '%s' is %s" % (title, rated))
    else:
        sys.stderr.write("Sorry, no Rotten Tomatoes rating available for title '%s'\n" % title)
        sys.exit(1)


if __name__ == "__main__":
    main()
