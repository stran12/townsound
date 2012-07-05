import oauth2 as oauth
import urlparse

consumer_key = 'key'
consumer_secret = 'secret'

request_token_url = 'http://term.ie/oauth/example/request_token.php'
access_token_url  = 'http://term.ie/oauth/example/access_token.php'
authorize_url     = 'http://term.ie/oauth/example/echo_api.php'

consumer = oauth.Consumer(consumer_key, consumer_secret)

client = oauth.Client(consumer)

resp, content = client.request(request_token_url, "GET")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])


print resp
print content
#request_token = dict(urlparse.parse_qsl(content))
#
#print "Request Token:"
#print "    - oauth_token        = %s" % request_token['oauth_token']
#print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
#print
#
#print "Go to the following link in your browser:"
#print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
#print 
#
#token = oauth.Token(request_token['oauth_token'],
#    request_token['oauth_token_secret'])
#token.set_verifier(oauth_verifier)
#client = oauth.Client(consumer, token)
#
#resp, content = client.request(access_token_url, "POST")
#access_token = dict(urlparse.parse_qsl(content))
#
#print "Access Token:"
#print "    - oauth_token        = %s" % access_token['oauth_token']
#print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
#print
#print "You may now access protected resources using the access tokens above." 
#print



