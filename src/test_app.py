from h2o_wave import main, app, Q, ui

# Locust configs
locustHost = 'localhost'
locustPort = '8089'

@app('/app')
async def serve(q: Q):
    if q.args.showLocust:
        locustpage(q)
    else:
        home(q)
    await q.page.save()


def home(q: Q):
    q.page['home'] = ui.form_card(box='1 1 5 20', items=[
        ui.text_xl(content='Load Testing Application for www.bbc.com'),
        ui.text_l(content='with H2O Wave and locust'),
        ui.image(
            title='h2o logo',
            path='https://www.h2o.ai/wp-content/uploads/2020/12/wave-type-yellow-1024x410.png',
            width='400px'
        ),
        ui.image(
            title='locust logo',
            path='http://localhost:8089/static/img/logo.png?v=2.5.0',
        ),
        
        ui.button(name='showLocust', label='Start', primary=True),
    ])

def locustpage(q: Q):
    q.page['loctus'] = ui.frame_card(
        box='1 1 10 100',
        title='Results',
        path='http://' + locustHost + ':' + locustPort + '/'
    )