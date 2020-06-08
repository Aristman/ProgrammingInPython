import re

html = 'Курс евро на сегодня 2,7432, курс евро на завтра 1,8543'
match = re.search(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
rate = match.group(1)
print(rate)
match2 = re.search(r'Евро.*(\d+,\d+)', html, re.IGNORECASE)
print(match2.group(1))
match = re.findall(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
print(match)
match = re.findall(r'Евро\D+(\d+),(\d+)', html, re.IGNORECASE)
print(match)
match = re.findall(r'Евро\D+\d+,\d+', html, re.IGNORECASE)
print(match)
match = re.findall(r'Евро\D+((\d+),(\d+))', html, re.IGNORECASE)
print(match)

html = """
 <a href="#" rel="nofollow">Курсы валют</a>
                        </dt>
                        <dd>
                            <table>
                                <tr>
                                    <th></th>
                                    <th>
06.06.20                                    </th>
                                    <th>
                                            <i>07.06.20</i>
                                    </th>
                                </tr>
                                    <tr>
                                        <td>EUR 1 Евро</td>
                                        <td>2,7028</td>
                                        <td>2,7028</td>
                                    </tr>
                                    <tr>
                                        <td>USD 1 Доллар США</td>
                                        <td>2,3810</td>
                                        <td>2,3810</td>
                                    </tr>
                                    <tr>
                                        <td>RUB 100 Российских рублей</td>
                                        <td>3,4695</td>
                                        <td>3,4695</td>
                                    </tr>
                            </table>
                            <p><a href="statistics/rates/ratesdaily.asp">подробнее</a></p>
                        </dd>
                    </dl>"""
match = re.findall()