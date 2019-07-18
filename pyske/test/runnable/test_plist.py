from pyske.core.list.slist import SList
from pyske.core.runnable.list.plist import PList

def test_init_to_seq_empty():
    pl = PList()
    res = pl.to_seq()
    exp = []
    assert res == exp


def app(l1, l2):
    return SList(l1 + l2)


msg = "hello world!"

def test_init_to_seq_non_empty():
    pl = PList.init(lambda i: msg[i], len(msg))
    res = pl.to_seq()
    exp = list(msg)
    assert res == exp


def test_map_empty():
    f = lambda x: x.upper()
    input = PList()
    res = input.map(f).to_seq()
    exp = []
    assert res == exp


def test_map_non_empty():
    f = lambda x: x.upper()
    input = PList.init(lambda i: msg[i], len(msg))
    res = input.map(f).to_seq()
    exp = list(f(msg))
    assert res == exp


def test_mapi_empty():
    f = lambda i, x: f'{i}:{x.upper()}'
    input = PList()
    res = input.mapi(f).to_seq()
    exp = []
    assert res == exp

# -------------------------- #


def test_reduce_nil():
    e = 0
    sl = SList()
    pl = PList.from_seq(sl)
    f = lambda x, y: x + y
    res = pl.reduce(f, e)
    exp = e
    assert res == exp


def test_reduce_cons():
    sl = SList([1, 2, 3, 4])
    pl = PList.from_seq(sl)
    f = lambda x, y: x + y
    res = pl.reduce(f)
    exp = 10
    assert res == exp


def test_reduce_sum_empty():
    e = 0
    sl = SList()
    pl = PList.from_seq(sl)
    f = lambda x, y: x + y
    exp = e
    res = pl.reduce(f, e)
    assert res == exp


def test_reduce_sum_non_empty():
    sl = SList([1, 2, 3, 4, 5, 6])
    pl = PList.from_seq(sl)
    f = lambda x, y: x + y
    exp = 21
    res = pl.reduce(f, 0)
    assert res == exp


# -------------------------- #

def test_map_reduce_nil():
    e = 0
    sl = SList()
    pl = PList.from_seq(sl)
    f = lambda x: x + 1
    op = lambda x, y: x + y
    res = pl.map_reduce(f, op, e)
    exp = e
    assert res == exp


def test_map_reduce_cons():
    sl = SList([1, 2, 3, 4])
    pl = PList.from_seq(sl)
    f = lambda x: x + 1
    op = lambda x, y: x + y
    res = pl.map_reduce(f, op)
    exp = pl.map(f).reduce(op)
    assert res == exp

# -------------------------- #

def test_mapi_non_empty():
    f = lambda i, x: f'{i}:{x.upper()}'
    input = PList.init(lambda i: msg[i], len(msg))
    res = input.mapi(f).to_seq()
    exp = SList(msg).mapi(f)
    assert res == exp


def test_scanr_non_empty():
    f = lambda x, y: x + y
    size = 23
    input = PList.init(lambda i: i, size)
    res = input.scanr(f).to_seq()
    exp = SList(range(0, size)).scanr(f)
    assert res == exp


def test_scanl_empty():
    f = lambda x, y: x + y
    size = 0
    input = PList.init(lambda i: i, size)
    res = input.scanl(f, 0).to_seq()
    exp = SList(range(0, size)).scanl(f, 0)
    assert res == exp


def test_scanl_non_empty():
    f = lambda x, y: x + y
    size = 23
    input = PList.init(lambda i: i, size)
    res = input.scanl(f, 0).to_seq()
    exp = SList(range(0, size)).scanl(f, 0)
    assert res == exp
