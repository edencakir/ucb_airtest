import sys
import requests
import urllib

def download_and_save_apk(url, build_number):
    r = requests.get(url, allow_redirects=True)
    open('build_{}.apk'.format(build_number), 'wb').write(r.content)

# get from bash
orgid = sys.argv[1]
projectid = sys.argv[2]
buildtargetid = sys.argv[3]
apikey = sys.argv[4]
url = "https://build-api.cloud.unity3d.com/api/v1/orgs/{}/projects/{}/buildtargets/{}/builds".format(orgid, projectid, buildtargetid)
print(url)
r = requests.get(url, headers={'Authorization': 'Basic {}'.format(apikey)})
print(r.status_code)
print(r.headers['content-type'])
data = r.json()

# find and download the latest successful build.
for build in data:
    if build["buildStatus"] == "success":
        build_number = build["build"]
        link = build["links"]["download_primary"]["href"]
        print(link)
        download_and_save_apk(link, build_number)
        break


