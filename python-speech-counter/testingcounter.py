using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace RegexTest
{
    class Program
    {
        static void Main()
        {
            string filename = @"c:\temp\speech.txt";

            string pattern = @"[\S]+";
            Regex rgx = new Regex(pattern, RegexOptions.IgnoreCase);

            int matchCount = 0;
            string[] lines = File.ReadAllLines(filename);
            {
                foreach(var line in lines )
                {
                    MatchCollection matches = rgx.Matches(line);
                    matchCount += matches.Count;

                    //if (matches.Count > 0)
                    //{
                    //    Console.WriteLine("{0} ({1} matches):", line, matches.Count);
                    //    foreach (Match match in matches)
                    //        Console.WriteLine("   " + match.Value);
                    //}
                }
            }
            Console.WriteLine("total words " + matchCount);

            NoRegex();
            Console.ReadLine();
        }

        static void NoRegex()
        {
            string filename = @"c:\temp\speech.txt";

            string text = File.ReadAllText(filename);
            text = text.Replace("\t", " ");
            text = text.Replace(".", " . ");
            text = text.Replace(",", " , ");
            text = text.Replace(";", " ; ");
            text = text.Replace("$", " $ ");
            text = text.Replace("[", " [ ");
            text = text.Replace("]", " ] ");
            text = text.Replace("?", " ? ");
            text = text.Replace("\"", " \" ");
            text = text.Replace("\r" , " ");
            text = text.Replace("\n", " ");
            text = text.Replace(""+'\xa0', "");// zero width space
            text = text.Replace("" + '\x2028', ""); // Unicode Character 'LINE SEPARATOR'
            text = text.Replace("" + '\x2013', " - "); // 'EN DASH'
            text = text.Replace("" + '\x2026', " - ");// 'HORIZONTAL ELLIPSIS'

            text = text.Replace("0", " 0 ");
            text = text.Replace("1", " 1 ");
            text = text.Replace("2", " 2 ");
            text = text.Replace("3", " 3 ");
            text = text.Replace("4", " 4 ");

            text = text.Replace("5", " 5 ");
            text = text.Replace("6", " 6 ");
            text = text.Replace("7", " 7 ");
            text = text.Replace("8", " 8 ");
            text = text.Replace("9", " 9 ");

            int length;

            do
            {
                length = text.Length;
                text = text.Replace("  ", " ");
            } while (length != text.Length);

            string[] words = text.Split(' ');

            Dictionary<string, int> dictionaryStringCount = new Dictionary<string, int>();

            foreach (var word in words)
            {
                string lowerCaseWord = word.ToLower();
                if (!dictionaryStringCount.ContainsKey(lowerCaseWord))
                {
                    dictionaryStringCount.Add(lowerCaseWord, 0);
                }
                dictionaryStringCount[lowerCaseWord]++;
            }

            List<string> sortedWords = new List<string>(dictionaryStringCount.Keys);
            sortedWords.Sort();

            foreach (var word in sortedWords)
            {
              //  Console.WriteLine("" + word + ", " + dictionaryStringCount[word]);
            }

            //for (int x = 0; x < 30; x++)
            //{
            //    Debug.WriteLine(sortedWords[x]);
            //    for (int suspectWordindex = 0; suspectWordindex < sortedWords[x].Length; suspectWordindex++)
            //    {
            //        Debug.Write(string.Format("{0:x}", (int)sortedWords[x][suspectWordindex]));
            //        Debug.Write(" ");
            //    }
            //    Debug.WriteLine(" ");
            //}

            // how many words??

            int totalWords = 0;

            foreach (var word in sortedWords)
            {
                if (word.Length != 0 && word[0] >= 'a')
                {
                    totalWords += dictionaryStringCount[word];
                }
            }

            Console.WriteLine("total words " + totalWords);
            Console.ReadLine();
        }
    }
}