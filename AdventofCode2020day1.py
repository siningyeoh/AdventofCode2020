{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "['1765\\n', '1742\\n', '1756\\n', '1688\\n', '1973\\n', '1684\\n', '1711\\n', '1728\\n', '1603\\n', '1674\\n', '1850\\n', '1836\\n', '1719\\n', '1937\\n', '1970\\n', '1770\\n', '1954\\n', '1848\\n', '1885\\n', '1851\\n', '1474\\n', '1801\\n', '1769\\n', '1904\\n', '1906\\n', '1739\\n', '1717\\n', '1830\\n', '1985\\n', '1930\\n', '1791\\n', '1977\\n', '1713\\n', '1787\\n', '1773\\n', '1672\\n', '1750\\n', '1931\\n', '1807\\n', '1762\\n', '1835\\n', '1736\\n', '1979\\n', '1923\\n', '1782\\n', '1797\\n', '1822\\n', '1903\\n', '1729\\n', '343\\n', '1678\\n', '1753\\n', '1873\\n', '1358\\n', '1987\\n', '1821\\n', '1761\\n', '1988\\n', '1886\\n', '1669\\n', '857\\n', '1894\\n', '1404\\n', '1909\\n', '1789\\n', '1752\\n', '1882\\n', '1969\\n', '1892\\n', '1701\\n', '1956\\n', '1839\\n', '483\\n', '1897\\n', '1730\\n', '1829\\n', '1879\\n', '1810\\n', '1755\\n', '1799\\n', '1932\\n', '1715\\n', '1809\\n', '418\\n', '1896\\n', '1691\\n', '1749\\n', '1922\\n', '1631\\n', '1780\\n', '1734\\n', '1859\\n', '1695\\n', '1548\\n', '1948\\n', '1997\\n', '1921\\n', '1994\\n', '1369\\n', '1364\\n', '1764\\n', '1697\\n', '1833\\n', '1239\\n', '616\\n', '1786\\n', '1890\\n', '677\\n', '1867\\n', '1705\\n', '1993\\n', '1925\\n', '1774\\n', '1732\\n', '1686\\n', '1847\\n', '1911\\n', '1841\\n', '1962\\n', '1907\\n', '1919\\n', '1725\\n', '1687\\n', '1236\\n', '1864\\n', '1855\\n', '1928\\n', '1941\\n', '1709\\n', '1683\\n', '1676\\n', '1889\\n', '1982\\n', '1595\\n', '1735\\n', '1857\\n', '1731\\n', '1816\\n', '2003\\n', '1724\\n', '741\\n', '1655\\n', '1308\\n', '1959\\n', '1955\\n', '1768\\n', '1795\\n', '1804\\n', '1961\\n', '1693\\n', '1884\\n', '1813\\n', '1927\\n', '1845\\n', '1689\\n', '1646\\n', '1803\\n', '2008\\n', '1599\\n', '1984\\n', '1871\\n', '1814\\n', '1918\\n', '1990\\n', '1858\\n', '1908\\n', '1949\\n', '1980\\n', '1618\\n', '1718\\n', '1712\\n', '1989\\n', '1876\\n', '1947\\n', '1974\\n', '1838\\n', '1865\\n', '1842\\n', '1817\\n', '680\\n', '1986\\n', '1812\\n', '1895\\n', '1991\\n', '1644\\n', '1877\\n', '1880\\n', '1792\\n', '1800\\n', '1899\\n', '1806\\n', '1699\\n', '1685\\n', '1793\\n', '1647\\n', '1429\\n', '1751\\n', '1722\\n', '1887\\n', '1968']\n"
     ]
    }
   ],
   "source": [
    "import itertools \n",
    "\n",
    "# store the input data into a variable \n",
    "# good practice guide in https://www.computerhope.com/issues/ch001721.htm\n",
    "expenses = []\n",
    "with open ('AdventofCode2020Day1.txt', 'rt') as AoCinput:   \n",
    "    for expense in AoCinput:\n",
    "        expenses.append(expense)\n",
    "print(expenses)                                             \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "[('1765\\n', '1742\\n'),\n",
       " ('1765\\n', '1756\\n'),\n",
       " ('1765\\n', '1688\\n'),\n",
       " ('1765\\n', '1973\\n'),\n",
       " ('1765\\n', '1684\\n')]"
      ]
     },
     "metadata": {},
     "execution_count": 2
    }
   ],
   "source": [
    "#make a list of all possible combinations of two values in sorted order from the input data\n",
    "combsp1 = list(itertools.combinations(expenses, 2))\n",
    "            \n",
    "combsp1[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "1404\n 616\n\n"
     ]
    }
   ],
   "source": [
    "#find ALL combinations which sum up to 2020\n",
    "for comb in combsp1:\n",
    "    if int(comb[0]) + int(comb[1]) == 2020:\n",
    "        print ((comb[0]),(comb[1]), sep=' ')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "864864\n"
     ]
    }
   ],
   "source": [
    "#multiply combinations which sum up to 2020\n",
    "for comb in combsp1:\n",
    "    if int(comb[0]) + int(comb[1]) == 2020:\n",
    "        print (int(comb[0])*int(comb[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "281473080\n"
     ]
    }
   ],
   "source": [
    "#repeat above but in a function and for combinations of 3\n",
    "def main():\n",
    "    combsp2 = list(itertools.combinations(expenses, 3))\n",
    "    for comb in combsp2:\n",
    "        if int(comb[0]) + int(comb[1]) + int(comb[2]) == 2020:\n",
    "            print (int(comb[0])*int(comb[1])*int(comb[2]))\n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}