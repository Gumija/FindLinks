using System;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Xml.Linq;
using HtmlAgilityPack;

namespace FindUrl
{
    class Program
    {
        static void Main(string[] args)
        {

            var text = readFile();
            parseWithRegex(text);
            parseWithXml(text);
        }

        private static void parseWithXml(string text)
        {
            var s1 = Stopwatch.StartNew();
            var htmlDoc = new HtmlDocument();
            htmlDoc.LoadHtml(text);
            var anchors = htmlDoc.DocumentNode.SelectNodes("//a");
            var links = anchors.Select(a => a.Attributes["href"].Value);
            s1.Stop();
            var duration = (double)(s1.ElapsedTicks) / TimeSpan.TicksPerSecond;
            System.Console.WriteLine($".Net Core HtmlAgilityPack Parse\t\tDuration: {duration:0.000000000}\t Found: {links.Count()}");
        }

        static Regex linkFinder = new Regex("<a.*href=\"(.*)\".*>", RegexOptions.Compiled);

        private static void parseWithRegex(string text)
        {
            var s1 = Stopwatch.StartNew();
            var match = linkFinder.Matches(text);
            s1.Stop();
            var duration = (double)(s1.ElapsedTicks) / TimeSpan.TicksPerSecond;
            System.Console.WriteLine($".Net Core Regex\t\t\t\tDuration: {duration:0.000000000}\t Found: {match.Count}");
        }

        static string readFile(){
            return File.ReadAllText(@"index.html");
        }
    }
}
