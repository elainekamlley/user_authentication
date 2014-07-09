(1) In web app security, what's the difference between "authorization" and "authentication"?
	
	Authentication verifies a user is who they claim to be, and authorization determines what an authenticated user is allowed to do. 
	Authentication is used to refer to both of these tasks. 

(2)The docs say that users' passwords get stored as "hash"es, not strings of the text they actually typed in. What's a hash?
	
	It is a one way function. It will take your password and run it through a algoritum to iterate a 'hash'. The hash generated can only be traced through the password and not the other way around.  

(3) Why do you think Django's auth system doesn't just let us see users' passwords in the database, stored as strings?
	
	It is a simple function that generates a unique collection of numbers and letters. This provides additional security for your users and safety rather than having plain text passwords. 
	
(4) What's OAuth (not necessary for Django, though you can use it)? This is a big thing to know about in open source software
	
	Is a process for resource owners (database, info, etc.) to authorize a third party access to their server resources without sharing their creditials or passwords. OAuth is commonly used as a way for web surfers to log into third party web sites using their Google, Facebook or Twitter accounts, without worrying about their access credentials being compromised.
