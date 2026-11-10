---
# Synced from https://docs.zid.sa/responses
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-responses
title: "Responses"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/responses
tags: [from-docs-site, partner-docs]
language: en
---

> Responses - Zid Docs
# Responses

**API Response Codes, Error Handling, and Best Practices**

Zid API is built to adhere strictly to REST principles, ensuring seamless communication between clients and our server. Below is a detailed guide to understanding the various HTTP response codes, error handling mechanisms, and best practices to help developers efficiently interact with our API.

## Success Response Codes #

We use standard HTTP response codes to indicate the status of API requests. Here’s a breakdown of the success codes:

**Color Code** **Response** **Status** **Meaning** **When to Use**

200 OK The request was successful, and the server returned the requested data. Use this when everything went as expected, and you’re returning data.

201 Created The request was successful, and a new resource was created. Use this when a new resource has been added to the database.

202 Accepted The request has been accepted for processing, but the processing is not complete. Use this for asynchronous processes where the action hasn’t completed yet.

204 No Content The request was successful, but there is no content to return. Use this when the action has been successfully executed, but there’s no content to send back.

### **Example Success Response:** #

A typical successful response would look like this:

```
` {
"status" : 200 ,
"success" : true ,
"data" : {
"message" : "Request processed successfully." ,
"code" : 200
}
} `
```

## Client Error Response Codes #

When a request fails due to client-side issues, the API will return a 4xx error code. Understanding these codes is crucial for diagnosing problems quickly.

**Color Code** **Response** **Slug** **Status** **Meaning** **Troubleshooting Tips**

400 bad_request Bad Request The server could not understand the request due to invalid syntax. Check the request syntax and parameters. Ensure all required fields are included.

401 unauthorized Unauthorized Authentication is required and has failed or has not yet been provided. Verify API keys or authentication credentials.

403 forbidden Forbidden The server understood the request but refuses to authorize it. Ensure the user has the necessary permissions.

404 not_found Not Found The requested resource could not be found. Double-check the URL and resource ID.

405 method_not_allowed Method Not Allowed The method specified in the request is not allowed. Verify that you are using the correct HTTP method (GET, POST, etc.).

406 not_acceptable Not Acceptable The server cannot produce a response matching the list of acceptable values defined in the request's headers. Adjust the `Accept` headers in your request.

410 gone Gone The resource requested is no longer available and will not be available again. This resource has been permanently removed, and you should clean up references to it.

422 validation_failed Unprocessable Entity The server understands the content type and syntax of the request entity, but it was unable to process the contained instructions. Review the data being submitted for missing fields or incorrect formats.

429 too_many_requests Too Many Requests You have sent too many requests in a given amount of time. Implement retry logic or reduce the request rate.

### Example Client Error Response: #

When the request is invalid, you might receive a response like this:

```
` {
"status" : 422 ,
"success" : false ,
"error" : {
"code" : "validation_failed" ,
"message" : "Invalid input data." ,
"fields" : {
"email" : [
"Email format is invalid."
] ,
"password" : [
"Password must be at least 8 characters."
]
}
}
}
`
```

## Server Error Response Codes #

Server errors indicate a problem with the server processing the request. These errors are generally not caused by the client.

**Color Code** **Response** **Slug** **Status** **Meaning** **Troubleshooting Tips**

500 server_error Internal Server Error The server encountered an unexpected condition that prevented it from fulfilling the request. Retry the request later. If the issue persists, contact support.

503 service_unavailable Service Unavailable The server is not ready to handle the request, often due to temporary overloading or maintenance. Wait and retry the request later.

### **Example Server Error Response:** #

In case of a server error, you might receive the following response:

```
` {
"status" : 500 ,
"success" : false ,
"error" : {
"code" : "server_error" ,
"message" : "An unexpected error occurred. Please try again later."
}
} `
```

## Handling Multiple Errors in 4xx Responses #

When a request results in multiple errors leading to a 4xx response, our API returns a structured response that includes a list of affected fields and an array of associated error messages. This helps in pinpointing the exact issues for each field.

### **Example of a Single Field Error:** #

```
` {
"status" : 422 ,
"success" : false ,
"error" : {
"code" : "خطأ في التحقق" ,
"message" : "تحتوي بعض الحقول على بيانات غير صحيحة." ,
"fields" : {
"اسم_المستخدم" : [
"اسم المستخدم مطلوب."
]
}
}
}
`
```

### Example of Multiple Field Errors: #

```
` {
"status" : 422 ,
"success" : false ,
"error" : {
"code" : "خطأ في التحقق" ,
"message" : "تحتوي عدة حقول على بيانات غير صحيحة." ,
"fields" : {
"اسم_المستخدم" : [
"اسم المستخدم مطلوب."
] ,
"البريد_الإلكتروني" : [
"صيغة البريد الإلكتروني غير صحيحة."
] ,
"كلمة_المرور" : [
"يجب أن تتكون كلمة المرور من 8 أحرف على الأقل."
] ,
"تأكيد_كلمة_المرور" : [
"تأكيد كلمة المرور غير متطابق."
]
}
}
}
`
```

## Best Practices for API Integration #

To ensure smooth interaction with our API, follow these best practices:

1 .

**Validate Inputs:** Always validate inputs before sending a request to minimize errors.

2 .

**Handle Rate Limits Gracefully:** Implement exponential backoff strategies to handle `429 Too Many Requests` responses.

3 .

**Check for Updates:** Periodically check for API updates to stay aligned with the latest changes and enhancements.

4 .

**Use Correct HTTP Methods:** Ensure you are using the appropriate HTTP methods (GET, POST, PUT, DELETE) as per the endpoint requirements.

5 .

**Test in a Safe Environment:** Before deploying changes in production, thoroughly test your integration in a development or staging environment.

## **Troubleshooting Tips for Developers:** #

💡**Check Response Headers:** Often, additional context is provided in response headers. Always review these when debugging issues.

💡**Log All Requests:** Maintain logs of all requests and responses, particularly during development, to track down issues more efficiently.

Modified at 2026-07-30 11:49:13

Previous

🚀 Start Here

Next

Rate Limiting
