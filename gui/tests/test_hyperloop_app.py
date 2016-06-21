import hypothesis
import hyperloop_app as app

def test_parse_args():
    test = ['localhost', '6666']
    args = app.parse_args(test).__dict__
    gold = {
        'log': 2,
        'local_udp_port': '8000',
        'remote_tcp_host': 'localhost',
        'remote_tcp_port': '6666',
    }
    assert args == gold

if __name__ == '__main__':
    test_parse_args()
