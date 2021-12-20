#!/usr/bin/perl
use POSIX qw(floor ceil);

my $str;

sub xexplode
# tar strengpos, rekdypde, lval som input, returnerer streng redusert
{
    my $strpos=$_[0];
    my $rd=$_[1];
    my $lval=$_[2];

    my $ss=substr($str,$strpos);

    my $si=index($ss,'[');

    print "strpos: $strpos $ss si:$si rd: $rd \n";

    if ($rd > length($str))
    {
	return 0;
    }

    # gjør om: om substrengen starter med par, og rd stor nok, eksploder.
    # ..
    
    
    if (substr($str,$strpos,1) eq "[")
    {

	if($rd > 4) #explode
	{
	    print "explode ss: $ss $rd\n";

	    if($ss=~/^\[(\d+),(\d+)\](\D\S+)/) #to tall
	    {
		my $lv=$1;
		my $rv=$2;
		my $rstr=$3;
		my $nstr;
		print "pair, explode: :$lv:$rv:$rstr:$rd:$strpos\n";

		my $lstr=reverse(substr($str,0,$strpos));
		print "pe lstr: $lstr\n";
		if($lstr=~/(\D+)(\d+)(\S+)/g) #tall til venstre?
		{
		    print "tall til v -$1-$2-$3-\n";
		    my $nlv=$lv+$2;
		    $nstr=reverse($3) . $nlv . reverse($1);
		}
		else
		{
		    $nstr=substr($str,0,$strpos);
		}

		print "nstr: -$nstr- rstr:$rstr\n";

		$nstr= $nstr . "0";

		if($rstr=~/(\D+)(\d+)(\S+)/g) #tall til høyre?
		{
		    print "tall til h -$1-$2-$3-\n";
		    my $nrv=$rv+$2;
		    $nstr= $nstr . $1 . $nrv . $3;
		}
		else
		{
		    $nstr= $nstr . $rstr;
		}

		print "nst2: -$nstr-\n";
		$str=$nstr;
		return 1;
	    }
	    else
	    {
		print "n3\n";
		return explode($strpos+1,$rd+1,$lval);

	    }
	    
	}
	else
	{
	    print "n1\n";
	    return explode($strpos+1,$rd+1,$lval);
	}
    }

    else
    {
	print "n2\n";
	return explode($strpos+$si,$rd,$lval);
    }
    return 0;
}

sub explode
{
    my $pos=0;
    my $level=0;
    # traverser $str til vi ser et tall..:
    do
    {
	my $c=substr($str,$pos,1);
	if ($c eq "[")
	{
	    $level++;
	}
	elsif($c eq "]")
	{
	    $level--;
	}
	else
	{
	    if($level > 4)
	    {
		my $ss=substr($str,$pos);
		if($ss=~/^(\d+),(\d+)](\S+)/)
		{
		    my $lv=$1;
		    my $rv=$2;
#		    print "exp, $level $pos -$1-$2-$3-$4\n";
		    my $rstr=$3;

		    my $lstr=reverse(substr($str,0,$pos));
#		    print "pe lstr: $lstr\n";
		    if($lstr=~/\[(\D+)(\d+)(\S+)/g) #tall til venstre?
		    {
#			print "tall til v -$1-$2-$3-\n";
			my $nlv=$lv+reverse($2);
			$nstr=reverse($3) . $nlv . reverse($1);
		    }
		    else
		    {
			$nstr=substr($str,0,$pos-1);
		    }

#		    print "nstr: -$nstr- rstr:$rstr\n";

		    $nstr= $nstr . "0";
		    
		    if($rstr=~/(\D+)(\d+)(\S+)/g) #tall til høyre?
		    {
#			print "tall til h -$1-$2-$3-\n";
			my $nrv=$rv+$2;
			$nstr= $nstr . $1 . $nrv . $3;
		    }
		    else
		    {
			$nstr= $nstr . $rstr;
		    }
#		    print "eend: $nstr\n";
		    $str=$nstr;
		    return 1;		    
		}
		else
		{
#		    print "no\n";
		}
	    }
	}
	$pos++;
    } while ($pos<length($str));
    return 0;
}

sub spl
{
    if($str=~/(\S+?)(\d{2,}?)(\S+)/)
    {
#	print "spl: _$1-$2-$3-\n";
	$str=$1 . "[" . floor($2 /2) . "," . ceil($2 / 2) . "]" . $3;
	return 1;
    }
    return 0;
}

sub mag
{

    while (	$str=~/(\S*?)\[(\d+),(\d+)](\S*$)/)
    {


	my $m = 3*$2 + 2*$3;
	$str = $1 . $m . $4;

    }
    print "mag:$str\n";
}

my $ostr=<>;
chomp $ostr;

while(<>)
{
    chomp;
 #   print "ostrnoe: $ostr\n";
    $str="[" . $ostr . "," . $_ . "]";

#    print "sstrnoe: $str\n";
    do
    {
	do
	{
#	    print "noe exp $str\n";
	} while ($noe=explode(0,0,-1));
		 
#	print "noe0str: $str\n";
	$noe=explode(0,0,-1);
#	print "noe1str: $str\n";
#	if(!$noe)
	{
	    $noe=$noe + spl;
	}
#	print "noe2str: $str\n";       
#	print "noe: $noe\n\n";
	
    } while ($noe);
    
    
    $ostr=$str;
}


print "line sstr: $str\n";
mag;

