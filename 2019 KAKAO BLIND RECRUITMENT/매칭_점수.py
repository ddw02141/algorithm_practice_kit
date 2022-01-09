from html.parser import HTMLParser
import re


class MyHTMLParser(HTMLParser):
    def __init__(self, word):
        HTMLParser.__init__(self)
        self.word = word.lower()
        self.domain = None
        self.external_urls = set()
        self.score = 0

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            for attr in attrs:
                if attr[0] == "content":
                    self.domain = attr[1]
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.external_urls.add(attr[1])

    # def handle_endtag(self, tag):
    #     print("Encountered an end tag :", tag)
    #
    def handle_data(self, data):
        prev_score = self.score
        data_lower = data.lower()
        if data_lower == self.word:
            self.score += 1
        else:
            start = re.findall("^" + self.word, data_lower)
            end = re.findall(self.word + "\Z", data_lower)
            mid = re.findall(r"(?=([^a-zA-Z]" + self.word + "[^a-zA-Z]))", data_lower)
            self.score = self.score + len(start) + len(end) + len(mid)


def solution(word, pages):
    parsers = list()
    domain_to_score = dict()
    domain_to_parser = dict()
    for page in pages:
        parser = MyHTMLParser(word)
        # print("parser.score:", parser.score)
        parser.feed(page)
        # print(parser.domain)
        # print(parser.external_urls)
        # print(parser.score)
        parsers.append(parser)
        domain_to_score[parser.domain] = parser.score
        domain_to_parser[parser.domain] = parser
    for i, parser in enumerate(parsers):
        score = 0 if len(parser.external_urls) == 0 else parser.score / len(parser.external_urls)
        for external_url in parser.external_urls:
            if external_url in domain_to_parser:
                external_parser = domain_to_parser[external_url]
                domain_to_score[external_parser.domain] += score
    max_score = -1
    for domain, score in domain_to_score.items():
        if score > max_score:
            max_score = score
        for parser in parsers:
            if parser.domain == domain:
                parser.score = score
    for i, parser in enumerate(parsers):
        if parser.score == max_score:
            return i


if __name__ == "__main__":
    print("------------------ Test Case 1 ------------------")
    sol = solution("blind", [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
    ans = 0
    assert ans == sol, f"Expected {ans} Actual {sol}"
    print("------------------ Test Case 2 ------------------")
    sol = solution("Muzi", [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"])
    ans = 1
    assert ans == sol, f"Expected {ans} Actual {sol}"
