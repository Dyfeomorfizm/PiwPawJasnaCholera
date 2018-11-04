import facebook
import credentials

def publish(msg):
  cfg = {
    "page_id"      : credentials.page_id,
    "access_token" : credentials.access_token
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_object(parent_object='me', connection_name='feed',message=msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
