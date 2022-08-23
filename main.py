last_etag = '0'

while True:
    r = requests.get(
        url,
        params={'last_etag': last_etag, 'wait_for_change': True},
        headers=METADATA_HEADERS)

    # During maintenance the service can return a 503, so these should
    # be retried.
    if r.status_code == 503:
        time.sleep(1)
        continue
    r.raise_for_status()

    last_etag = r.headers['etag']
    

