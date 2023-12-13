use std::fs::File;
use std::io::Read;

fn get_location(tr: &Vec<Vec<Vec<i64>>>, cxr: i64) -> i64 {
    let mut cur = cxr;
    for trc in tr {
        let mut nxt = -1;
        for line in trc {
            if line[1] <= cur && cur < line[1] + line[2] {
                nxt = line[0] + cur - line[1];
                break;
            }
        }
        if nxt == -1 {
            nxt = cur;
        }
        // print!("{} ", cur);
        cur = nxt;
    }
    cur
}

fn main() {
    let mut f = File::open("input_day5.txt").expect("Failed to open file");
    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("Failed to read file");

    let k: Vec<&str> = contents.split("\n\n").collect();
    let seeds: Vec<i64> = k[0][7..]
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut tr: Vec<Vec<Vec<i64>>> = Vec::new();
    for z in k[1..].iter() {
        let trc: Vec<Vec<i64>> = z
            .lines()
            .skip(1)
            .map(|line| {
                line.split_whitespace()
                    .map(|x| x.parse().unwrap())
                    .collect()
            })
            .collect();
        tr.push(trc);
    }

    // Part 1
    // let min_location = seeds
    //     .iter()
    //     .map(|&seed| get_location(&tr, seed))
    //     .min()
    //     .unwrap();
    // println!("{}", min_location);

    // println!("{}", get_location(&tr, 1643652834));

    // Part 2
    let mut res = i64::MAX;
    for i in 0..seeds.len() / 2 {
        for (index, j) in (seeds[i * 2]..(seeds[i * 2] + seeds[i * 2 + 1])).enumerate() {
            if index % 100000000 == 0 {
                println!(
                    "{} of {}, {} of {} value {}",
                    i,
                    seeds.len() / 2,
                    index,
                    seeds[i * 2 + 1],
                    res
                );
            }
            res = res.min(get_location(&tr, j));
        }
    }
    println!("{}", res);
}
