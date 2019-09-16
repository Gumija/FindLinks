use regex::Regex;
use std::time::Instant;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let html = read_html();
    find_all_links(&html);
}

fn read_html() -> String {
    let mut file = File::open("index.html").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents;
}

fn find_all_links(html:&str){
    println!("Rust Regex");
    let now = Instant::now();
    let re = Regex::new("<a.*href=\"(.*)\".*>").unwrap();
    let iter = re.find_iter(html);
    let dur = now.elapsed();
    let result = format!("Duration: {s}.{sub:09}\t\t Found: {f}", f = iter.count(), s = dur.as_secs(), sub = dur.subsec_nanos() );
    println!("{}", result);
}