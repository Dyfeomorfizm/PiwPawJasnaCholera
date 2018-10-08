import facebook

def main():
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "354252548451865",  # Step 1
    "access_token" : "EAAOexbWKpeEBAD6lmGZCdOA56nbvZAIFZBmZBU2K4LNMKc56Gofq3sxv7YIxclZCmXpOMbeuV88w4kEIk7uyaTMdrsCtIpcRysdALvhTuMhkbzQ4kgR5h05jgGDRgOqX1eCdMWoDd9ZCE8D35VVKS3OcIETpEQdOGpj47kwbRk3qou8wXpnZC3HpHzAjLTfWPyQDY9kh7JuUQZDZD"   # Step 3
    }

  api = get_api(cfg)
  msg = "Hello, world!"
  status = api.put_object(parent_object='me', connection_name='feed',message=msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  main()