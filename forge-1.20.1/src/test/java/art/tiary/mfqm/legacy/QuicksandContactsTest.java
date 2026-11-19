package art.tiary.mfqm.legacy;
import org.junit.jupiter.api.Test;
import java.nio.file.*;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;
class QuicksandContactsTest {
    @Test void allEvidenceDecisionVectors() throws Exception {
        var rows=Files.readAllLines(Path.of("src/test/resources/phase8/quicksand-contact.tsv"));
        assertEquals(72,rows.size());
        for(var row:rows){
            var c=row.split("\t");var actual=new ArrayList<Integer>();
            QuicksandContacts.emit(Double.parseDouble(c[0]),0,Boolean.parseBoolean(c[1]),Boolean.parseBoolean(c[2]),Boolean.parseBoolean(c[3]),actual::add);
            List<Integer> expected=c[4].equals("-")?List.of():Arrays.stream(c[4].split(";")).map(Integer::parseInt).toList();
            assertEquals(expected,actual,row);
        }
    }
}
