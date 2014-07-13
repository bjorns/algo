mod unionfind;

#[test]
fn test_create_unionfind() {
    let mut uf: ::unionfind::UnionFind<uint> = ::unionfind::new();
    assert!(0 == uf.size());
    let ticket = uf.add(4711i);
    assert!(1 == uf.size());
    let y = uf.find(ticket);
    assert!(4711 == y);
}


#[test]
fn test_union() {
    let mut uf: ::unionfind::UnionFind<uint> = ::unionfind::new();
    let ticket0 = uf.add(4711i);
    let ticket1 = uf.add(4712i);
    assert!(2 == uf.clusters());
    assert!(4711u == uf.find(ticket0))
    assert!(4712u == uf.find(ticket1))

    uf.union(ticket0, ticket1);
    assert!(1 == uf.clusters());

    assert!(4712 == uf.find(ticket0));
    assert!(4712 == uf.find(ticket1));
}
