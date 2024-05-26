Explanation
Upon opening the website's homepage in BurpSuite, we observed an admin cookie in the response, represented as "68934a3e9455fa72420237eb05902327." This value, when decoded using the MD5 hashing algorithm, translates to "false."

To proceed, we encoded the value "true" using MD5, resulting in "b326b5062b2f0e69046810717534cb09." With BurpSuite's intercept feature enabled, we replaced the original cookie value with the newly generated MD5 hash. By forwarding the request, we were able to successfully obtain the flag.