use std::io::File;
use std::io::BufferedReader;

use std::string::String;
use std::os;


mod unionfind;

fn atoi(ch: char) -> uint {
    return if ch == '1' {
        1
    } else {
        0
    };
}

fn to_uint(mut str: String) -> uint {
    let mut ret: uint = 0u;
    let mut pos = 1;
    loop {
        let opt_ch = str.pop_char();
        if opt_ch == None {
            break;
        }
        let ch = opt_ch.unwrap();
        if ch != ' ' {
            let bit = atoi(ch);

            ret += bit * pos;

        }
        pos *= 2;
    }
    return ret;
}

fn parse_numbers(file: File) -> Vec<uint> {
    let mut ret: Vec<uint> = vec!();
    let mut lineno = 0;
    for line in BufferedReader::new(file).lines() {
        if lineno != 0 {
            let s = line.unwrap();
            let number = to_uint(s.clone());
            ret.push(number);
        }
        lineno += 1
    }
    return ret;
}

fn init_unionfind(data: &Vec<uint>) -> unionfind::UnionFind<uint> {
    let mut uf: unionfind::UnionFind<uint> = unionfind::new();
    for x in data.iter() {
        uf.add(x);
    };
    return uf;
}

fn hamming_neighbours(x: uint, radix: uint) -> Vec<uint> {
    let mut ret: Vec<uint> = vec!();
    for i in range(0, radix) {
        let bit = 1 << i;
        ret.push(x | bit);
        ret.push_all(hamming_neighbours(x | bit, radix).as_slice());
    }
    return ret;
}

fn merge_neighbours(uf: unionfind::UnionFind<uint>, data: &Vec<uint>) {
    for x in data.iter() {
        let n = hamming_neighbours(*x, 24);

    }
}

fn main() {
    let args = os::args();
    let filename = args.get(1);
    let bytes = filename.clone().into_bytes();

    println!("Reading {}", filename);

    let path = Path::new(bytes);
    let mut file = File::open(&path);
    if file.is_ok() {
        let data = parse_numbers(file.ok().unwrap());
        let uf = init_unionfind(&data);

        merge_neighbours(uf, &data);
    }


    println!("hello!");
}
