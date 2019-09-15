use regex::Regex;
use std::time::Instant;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let html = read_html();
    find_all_links(&html);
}

fn read_html() -> String {
    let mut file = File::open("../index.html").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents;
}

fn find_all_links(html:&str){
    let now = Instant::now();
    let re = Regex::new("<a.*href=\"(.*)\".*>").unwrap();
    let iter = re.find_iter(html);
    let result = format!("Duration: {d}\t Found: {f}", f = iter.count(), d = now.elapsed().as_millis());
    println!("{}", result);
}