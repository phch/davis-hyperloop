import hypothesis
import hyperloop_app as app

def test_parse_args():
    test = ['localhost', '6666']
    args = app.parse_args(args).__dict__
    gold = {'ip': 'localhost', 'port': '6666', 'log': 2}
    assert args == gold

if __name__ == '__main__':
    test_parse_args()
