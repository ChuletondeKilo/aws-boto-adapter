
**Motivation**

1. Avoid boto3 calling system to each service.
2. Share a comfortable API to the user.
	- Remove .session() or .client() calls.
	- Validate user input values and keys based on what boto3 allows.
	- Expose docs to the user depending on the service and method call that he wants to use (at the very moment python does not show that when editing code).
	- Future implementation: Multithreading/async calls.
3. We can abstract the user to know what is a .session() and a .client() method. We simply expose specific actions that need some metadata.


**AIM**

User call like: aws_interface.ssm_adapter()