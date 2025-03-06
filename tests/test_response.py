import sys
sys.path.append("/Users/dshcherbachenia/development/pet/devPlanPresentation/terraform/lambdas/")
import main



def test_main():
    r = main.handler(None, None)
    
    assert r is not None
    assert len(r['body']) > 0
    assert r['statusCode'] == 200
    assert 'data' in r['body']