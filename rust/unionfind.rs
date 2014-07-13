struct Entry<T> {
    data: T,
    leader: uint,
    followers: Vec<uint>
}

impl<T: Clone> Entry<T> {
    fn clone(&self) -> Entry<T> {
        let copy: Entry<T> = Entry {
            data: self.data.clone(),
            leader: self.leader,
            followers: self.followers.clone()
        };
        return copy;
    }

    fn update(&mut self, new: Entry<T>) {
        self.data = new.data.clone();
        self.leader = new.leader;
        self.followers = new.followers.clone();
    }
}

fn new_entry<T>(data: T) -> Entry<T> {
    let e: Entry<T> = Entry {
        data: data,
        leader: -1,
        followers: vec![]
    };
    return e;
}


pub struct UnionFind<T> {
    num_clusters: uint,
    entries: Vec<Entry<T>>
}

pub fn new<T>() -> UnionFind<T> {
    let u: UnionFind<T> = UnionFind {
        num_clusters: 0,
        entries: vec![]
    };
    return u;
}

impl<T: Clone> UnionFind<T> {
    pub fn add<T>(&mut self, data: T) -> uint {
        let mut e = new_entry(data);
        let ticket: uint = self.entries.len();
        e.leader = ticket;
        self.entries.push(e);
        self.num_clusters += 1;
        return ticket;
    }

    pub fn clusters(&self) -> uint {
        return self.num_clusters
    }

    fn get_entry(&self, index: uint) -> Entry<T> {
        let entry = self.entries.get(index);
        return entry.clone();
    }

    pub fn find(&self, index: uint) -> T {
        let entry = self.entries.get(index);
        return self.get_entry(entry.leader).data;
    }


    pub fn union(&mut self, ticket0: uint, ticket1: uint) {
        let e0 = self.get_entry(ticket0);
        let e1 = self.get_entry(ticket1);

        assert!(e0.leader == ticket0) // Basic sanity check.
        assert!(e1.leader == ticket1)

        let (mut src, dst, src_index, dst_index): (Entry<T>, Entry<T>, uint, uint) =
        if e0.followers.len() > e1.followers.len() {
            (e1, e0, ticket1, ticket0)
        } else {
            (e0, e1, ticket0, ticket1)
        };

        for index in src.followers.iter() {
            self.entries.get_mut(*index).leader = dst_index;
            self.entries.get_mut(dst_index).followers.push(*index)
        }
        self.entries.get_mut(src_index).leader = dst_index;
        self.entries.get_mut(dst_index).followers.push(src_index);
        self.num_clusters -= 1;
    }

    pub fn size(&self) -> uint {
        return self.entries.len();
    }
}
