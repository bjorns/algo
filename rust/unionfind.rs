

mod unionfind {
    use std::collections::HashMap;
    use std::hash::Hash;
    use std::cmp::Eq;

    struct Entry<T> {
        data: T,
        followers: HashMap<T, T>
    }

    struct UnionFind<T> {
        next: uint,
        entries: Vec<Entry<T>>
    }

    fn new<T>() -> UnionFind<T> {
        let mut u: UnionFind<T> = UnionFind{
            next: 0,
            entries: vec![]
        };
        return u;
    }

    impl<T: Hash + Eq + Clone> UnionFind<T> {
        fn add<T: Hash + Eq>(&mut self, data: T) {
            let e: Entry<T> = Entry {
                data: data,
                followers: HashMap::new()
            };
            self.entries.push(e);
        }

        fn find(&self, index: uint) -> T {
            let x = self.entries.get(index);
            return x.data.clone();
        }
    }
}
