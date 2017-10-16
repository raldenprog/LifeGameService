
export const gcf = {}


gcf.Headers = new Headers(
  {'authorization': 'OAuth AQAAAAATte4MAASKz4HQt9ZVKk-zry4AXa7IrWc'})


gcf.apiHttp = 'https://cloud-api.yandex.net/v1/disk/resources?'


gcf.filedsParam = [
  '_embedded.items.path',
  '_embedded.items.name',
  '_embedded.items.type',
  '_embedded.items.size'
].join(',')
